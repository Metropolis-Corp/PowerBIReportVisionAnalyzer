import os
import base64
import requests
from dotenv import load_dotenv
from autogen.skill_base import Skill, SkillExecutionError


class ExportPowerBIReportAsImage(Skill):
    name = "ExportPowerBIReportAsImage"
    description = "Exports a Power BI report page as an image using the Power BI REST API."

    input_schema = {
        "type": "object",
        "properties": {
            "report_id": {"type": "string", "description": "ID of the Power BI report."},
            "page_name": {"type": "string", "description": "Name of the report page to export."},
            "export_format": {"type": "string", "description": "Export format (PNG or PDF).", "enum": ["PNG", "PDF"]}
        },
        "required": ["report_id", "page_name", "export_format"]
    }

    output_schema = {
        "type": "object",
        "properties": {
            "image_data": {"type": "string", "description": "Base64-encoded image data."}
        },
        "required": ["image_data"]
    }

    def execute(self, input_data):
        self.validate_input(input_data)
        report_id = input_data["report_id"]
        page_name = input_data["page_name"]
        # Ensure format is in the correct case
        export_format = input_data["export_format"].upper()

        try:
            access_token = self.get_powerbi_access_token()
            if not access_token:
                raise SkillExecutionError(
                    "Failed to obtain Power BI access token.")

            image_data = self.export_report_as_image(
                report_id, page_name, export_format, access_token)
            output_data = {"image_data": image_data}
            self.validate_output(output_data)
            return output_data
        except requests.exceptions.HTTPError as http_err:
            if http_err.response.status_code == 429:
                raise SkillExecutionError(
                    "API request rate limit exceeded, please try again later.")
            raise SkillExecutionError(
                f"HTTP Error during API call: {str(http_err)}")
        except Exception as e:
            raise SkillExecutionError(f"Error exporting report page: {str(e)}")

    def get_powerbi_access_token(self):
        load_dotenv()  # Load environment variables from .env file
        tenant_id = os.getenv("TENANT_ID")
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        scope = "https://analysis.windows.net/powerbi/api/.default"
        token_endpoint = f"https://login.microsoftonline.com/{
            tenant_id}/oauth2/v2.0/token"

        payload = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": scope
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        try:
            response = requests.post(
                token_endpoint, headers=headers, data=payload)
            response.raise_for_status()
            token_data = response.json()
            return token_data["access_token"]
        except requests.exceptions.RequestException as e:
            raise SkillExecutionError(
                f"Error obtaining Power BI access token: {str(e)}")

    def export_report_as_image(self, report_id, page_name, format, access_token):
        """
        Exports a Power BI report page as an image using the specified format and access token.
        """
        url = f"https://api.powerbi.com/v1.0/myorg/reports/{
            report_id}/pages/{page_name}/ExportTo"
        headers = {'Authorization': f'Bearer {access_token}'}
        params = {'format': format}

        try:
            response = requests.get(url, headers=headers, params=params)
            # This will throw an error if the request was unsuccessful
            response.raise_for_status()
            return base64.b64encode(response.content).decode('utf-8')
        except requests.exceptions.RequestException as e:
            raise SkillExecutionError(
                f"Error exporting report page as image: {str(e)}")


# Example usage
if __name__ == "__main__":
    skill_instance = ExportPowerBIReportAsImage()
    input_example = {
        "report_id": "example_report_id",
        "page_name": "report_page_name",
        "export_format": "PNG"
    }
    try:
        result = skill_instance.execute(input_example)
        print(result)
    except SkillExecutionError as e:
        print(f"Error executing skill: {str(e)}")
