import os

AZURE_OPENAI_DEPLOYMENT_NAME = "your-deployment-name"
GOOGLE_VERTEXAI_MODEL_NAME = "gemini-pro"

os.environ["OPENAI_API_VERSION"] = "2023-12-01-preview"
os.environ["AZURE_OPENAI_API_KEY"] = "api key"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://your-instance-name.openai.azure.com/"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-service-account-key-file"
