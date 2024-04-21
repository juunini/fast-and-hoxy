from langchain_openai import AzureChatOpenAI
from langchain_google_vertexai import ChatVertexAI
from langchain_core.language_models.chat_models import BaseChatModel

import config


def google_vertexai() -> BaseChatModel:
    model = ChatVertexAI(model_name=config.GOOGLE_VERTEXAI_MODEL_NAME)
    return model


def azure_openai() -> BaseChatModel:
    model = AzureChatOpenAI(
        azure_deployment=config.AZURE_OPENAI_DEPLOYMENT_NAME,
    )
    return model
