import logging
import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from configparser import ConfigParser
from cryptography.fernet import Fernet
import re

# Setup Logging
def setup_logger():
    logger = logging.getLogger(__name__)
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    logger.setLevel(log_level)
    handler = logging.FileHandler('api_data_fetcher.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()

# Define Custom Exceptions
class APIAuthenticationError(Exception):
    """Custom exception for API authentication errors."""

class APIRequestError(Exception):
    """Custom exception for API request errors."""

class APIResponseError(Exception):
    """Custom exception for API response errors."""

# Secure Configuration Management
def load_encrypted_config():
    config = ConfigParser()
    config.read('settings.ini')
    key = os.environ.get("CONFIG_ENCRYPTION_KEY")
    if not key:
        raise ValueError("CONFIG_ENCRYPTION_KEY environment variable is not set")
    fernet = Fernet(key)
    encrypted_value = config['api']['api_key']
    decrypted_value = fernet.decrypt(encrypted_value.encode()).decode()
    return decrypted_value

# Validate and Sanitize Inputs
def validate_input(input_data):
    if not input_data:
        raise ValueError("Input data is required")
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    if not pattern.match(input_data):
        raise ValueError("Invalid input format")
    sanitized_input = input_data.replace("'", "''").replace(";", "")
    return sanitized_input

# API Interaction and Data Extraction
class APIDataFetcher:
    def __init__(self, api_url):
        self.api_url = api_url
        self.api_key = load_encrypted_config()

    def get_data(self, input_params):
        sanitized_input = validate_input(input_params)
        headers = {'Authorization': f'Bearer {self.api_key}'}
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        with requests.Session() as session:
            session.mount("https://", adapter)
            response = session.get(self.api_url, params=sanitized_input, headers=headers, timeout=10)
            return self.handle_api_response(response)

    def handle_api_response(self, response):
        if response.status_code == 401:
            logger.error("API authentication failed")
            raise APIAuthenticationError("Invalid API credentials")
        elif response.status_code == 400:
            logger.error("Bad request to the API")
            raise APIRequestError("Invalid request parameters")
        elif response.status_code != 200:
            logger.error(f"API request failed with status code {response.status_code}")
            raise APIResponseError(f"Unexpected API response: {response.text}")
        return response.json()

# Unit Testing
import unittest
from unittest.mock import patch

class TestAPIDataFetcher(unittest.TestCase):
    @patch('skill.requests.Session.get')
    def test_successful_response(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "valid"}

        fetcher = APIDataFetcher("https://api.example.com")
        result = fetcher.get_data("valid_input")
        self.assertEqual(result, {"data": "valid"})

    @patch('skill.requests.Session.get')
    def test_authentication_error(self, mock_get):
        mock_get.return_value.status_code = 401

        fetcher = APIDataFetcher("https://api.example.com")
        with self.assertRaises(APIAuthenticationError):
            fetcher.get_data("valid_input")

    @patch('skill.requests.Session.get')
    def test_request_error(self, mock_get):
        mock_get.return_value.status_code = 400

        fetcher = APIDataFetcher("https://api.example.com")
        with self.assertRaises(APIRequestError):
            fetcher.get_data("invalid_input")

    @patch('skill.requests.Session.get')
    def test_response_error(self, mock_get):
        mock_get.return_value.status_code = 500

        fetcher = APIDataFetcher("https://api.example.com")
        with self.assertRaises(APIResponseError):
            fetcher.get_data("valid_input")

if __name__ == "__main__":
    unittest.main()
