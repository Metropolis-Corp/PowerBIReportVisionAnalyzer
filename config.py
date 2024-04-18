import os
from dotenv import load_dotenv

load_dotenv()

# Configuration for API connectivity
API_URL = os.getenv("API_URL")
if API_URL is None:
    raise ValueError("API_URL is not set in the environment variables.")

CONFIG_ENCRYPTION_KEY = os.getenv("CONFIG_ENCRYPTION_KEY")
if CONFIG_ENCRYPTION_KEY is None:
    raise ValueError("CONFIG_ENCRYPTION_KEY is not set in the environment variables.")

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Resource URLs for Azure services
RESOURCE_URL = "https://analysis.windows.net/powerbi/api"
SCOPE_URL = "https://analysis.windows.net/powerbi/api/.default"

# Additional Azure OpenAI settings
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_EMBEDDING_NAME = os.getenv("AZURE_OPENAI_EMBEDDING_NAME")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
AZURE_OPENAI_MODEL_NAME = os.getenv("AZURE_OPENAI_MODEL_NAME")
AZURE_OPENAI_RESOURCE = os.getenv("AZURE_OPENAI_RESOURCE")
API_VERSION = os.getenv("API_VERSION")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Optional variables with default values
DATASET_ID = os.getenv("DATASET_ID", "default_dataset_id")
