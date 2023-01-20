import pytest
from mock import MODEL_TYPE, KEY
from src.search.viewer import ConfigService, ChatGPTService


@pytest.fixture
def config_service():
    return ConfigService(MODEL_TYPE)


@pytest.fixture
def chat_gpt_service(config_service):
    service = ChatGPTService(KEY)
    service.conf_service = config_service
    return service
