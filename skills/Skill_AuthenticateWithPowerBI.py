import requests
import logging
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET, RESOURCE_URL, SCOPE_URL, DATASET_ID
import powerbi_client

class PowerBIAuthenticator:
    def __init__(self):
        self.tenant_id = TENANT_ID
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.resource = RESOURCE_URL
        self.scope = SCOPE_URL
        self.token_endpoint = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"

    def get_powerbi_access_token(self):
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "resource": self.resource,
            "scope": self.scope
        }
        try:
            response = requests.post(self.token_endpoint, data=payload)
            response.raise_for_status()
            token_data = response.json()
            return token_data.get("access_token")
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP Error obtaining access token: {e}")
        except Exception as e:
            logging.error(f"Error obtaining access token: {e}")
        return None

    def last_data_update_checker(self, dataset_id):
        access_token = self.get_powerbi_access_token()
        if not access_token:
            return {"error": "Failed to authenticate with Power BI API."}
        
        try:
            client = powerbi_client.connect(dataset_id, access_token)
            tables = client.get_tables(dataset_id)
            last_updates = self._get_last_updates(client, tables)
            return last_updates
        except Exception as e:
            logging.error(f"Error checking last data update: {e}")
            return {"error": "Failed to check last data update."}

    def _get_last_updates(self, client, tables):
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
