import logging
import requests
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET, RESOURCE_URL, SCOPE_URL, DATASET_ID
import powerbi_client

class PowerBIAuthenticator:
    """
    Handles authentication with Power BI and provides functionality to check last data updates on datasets.

    Attributes:
        tenant_id (str): Azure tenant ID for authentication.
        client_id (str): Registered client ID for authentication.
        client_secret (str): Client secret for OAuth2 authentication.
        resource (str): The resource URL for Power BI.
        scope (str): The scope of the OAuth2 request.
        token_endpoint (str): Endpoint for retrieving OAuth2 tokens.
    """

    def __init__(self):
        """Initialize the PowerBIAuthenticator with necessary credentials and endpoints from the configuration."""
        self.tenant_id = TENANT_ID
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.resource = RESOURCE_URL
        self.scope = SCOPE_URL
        self.token_endpoint = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"

    def get_powerbi_access_token(self):
        """Retrieve the Power BI API access token using client credentials.

        Returns:
            str: Access token if successful, None otherwise.
        """
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "resource": self.resource,
            "scope": self.scope
        }
        try:
            response = requests.post(self.token_endpoint, data=payload, timeout=10)
            response.raise_for_status()
            token_data = response.json()
            return token_data.get("access_token")
        except requests.exceptions.RequestException as e:
            logging.error("HTTP Error obtaining access token: %s", e)
        return None

    def last_data_update_checker(self, dataset_id):
        """Check the latest update timestamp for all tables in a given dataset.

        Args:
            dataset_id (str): The Power BI dataset ID to check.

        Returns:
            dict: Dictionary with table names and their latest update timestamps if successful, error message otherwise.
        """
        access_token = self.get_powerbi_access_token()
        if not access_token:
            return {"error": "Failed to authenticate with Power BI API."}
        
        try:
            client = powerbi_client.connect(dataset_id, access_token)
            tables = client.get_tables(dataset_id)
            return self._get_last_updates(client, tables)
        except Exception as e:
            logging.error("Error checking last data update: %s", e)
            return {"error": "Failed to check last data update."}

    def _get_last_updates(self, client, tables):
        """Retrieve the latest update date for each table in the dataset.

        Args:
            client (powerbi_client): Authenticated Power BI client.
            tables (list): List of tables in the dataset.

        Returns:
            dict: Dictionary with table names and their latest update dates.
        """
        last_updates = {}
        for table in tables:
            date_fields = [field for field in client.get_table_schema(table['name']) if field['type'] in ['date', 'datetime']]
            last_updates[table['name']] = {}
            for field in date_fields:
                query = f"SELECT TOP 1 {field['name']} FROM {table['name']} ORDER BY {field['name']} DESC"
                last_date = client.execute_query(query)
                last_updates[table['name']][field['name']] = last_date
        return last_updates

# Usage
if __name__ == "__main__":
    authenticator = PowerBIAuthenticator()
    updates = authenticator.last_data_update_checker(DATASET_ID)
    print(updates)
