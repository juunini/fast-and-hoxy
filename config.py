import os

AZURE_OPENAI_DEPLOYMENT_NAME = "your-deployment-name"

os.environ["OPENAI_API_VERSION"] = "2023-12-01-preview"
os.environ["AZURE_OPENAI_API_KEY"] = "api key"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://your-instance-name.openai.azure.com/"
