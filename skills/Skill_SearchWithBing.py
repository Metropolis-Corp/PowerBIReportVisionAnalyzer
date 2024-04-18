import requests
import re
import json
import logging
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from cryptography.fernet import Fernet
from configparser import ConfigParser
from config import API_URL, CONFIG_ENCRYPTION_KEY
import unittest
from unittest.mock import patch

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('bing_search_skill.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

class BingSearchError(Exception):
    """Custom exception for Bing Search API errors."""

def validate_input(input_data):
    if not input_data:
        raise ValueError("Search query is required")
    return re.sub("[^a-zA-Z0-9 ]", "", input_data)  # Improved sanitization

def load_encrypted_config():
    config_path = 'settings.ini'
    config = ConfigParser()
    config.read(config_path)
    if not CONFIG_ENCRYPTION_KEY:
        raise ValueError("CONFIG_ENCRYPTION_KEY environment variable is not set")

    fernet = Fernet(CONFIG_ENCRYPTION_KEY)
    encrypted_value = config['bing_search']['api_key']
    decrypted_value = fernet.decrypt(encrypted_value.encode()).decode()
    return decrypted_value

def handle_api_response(response):
    if response.status_code == 401:
        logger.error("Bing Search API authentication failed")
        raise BingSearchError("Invalid Bing Search API credentials")
    elif response.status_code == 400:
        logger.error("Bad request to the Bing Search API")
        raise BingSearchError("Invalid request parameters")
    elif response.status_code != 200:
        logger.error(f"Bing Search API request failed with status code {response.status_code}")
        raise BingSearchError(f"Unexpected Bing Search API response: {response.text}")

def search_bing_function(search_query, api_url=API_URL, timeout_seconds=10, retry_total=3, retry_status_forcelist=[429, 500, 502, 503, 504]):
    sanitized_query = validate_input(search_query)
    api_key = load_encrypted_config()
    headers = {"x-functions-key": api_key}

    retry_strategy = Retry(
        total=retry_total,
        status_forcelist=retry_status_forcelist,
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)

    params = {"q": sanitized_query}
    with requests.Session() as session:
        session.mount("https://", adapter)
        response = session.get(api_url, params=params, headers=headers, timeout=timeout_seconds)
        handle_api_response(response)
    return response.json()

class TestBingSearchSkill(unittest.TestCase):
    @patch('requests.get')
    def test_successful_response(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = json.dumps([{"name": "Test Result"}]).encode()
        mock_get.return_value = mock_response
        
        result = search_bing_function("test query")
        self.assertEqual(result, [{"name": "Test Result"}])
    
    @patch('requests.get')
    def test_authentication_error(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 401
        mock_get.return_value = mock_response
        
        with self.assertRaises(BingSearchError):
            search_bing_function("test query")
    
    @patch('requests.get')
    def test_request_error(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 400
        mock_get.return_value = mock_response
        
        with self.assertRaises(BingSearchError):
            search_bing_function("test query")
    
    @patch('requests.get')
    def test_response_error(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        with self.assertRaises(BingSearchError):
            search_bing_function("test query")

if __name__ == "__main__":
    unittest.main()
