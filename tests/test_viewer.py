from mock import MODEL_NAME, SHORT_QUERY, LONG_QUERY, ModelTypes, CODE_QUERY, UNKNOWN


def test_get_conf(config_service):
    conf = config_service.get_conf()
    assert conf["model"] == MODEL_NAME


def test_get_model_types(config_service):
    assert config_service.get_model_type(SHORT_QUERY) == ModelTypes.TEXT_QA.value
    assert config_service.get_model_type(LONG_QUERY) == ModelTypes.TEXT_LONG_QA.value
    assert config_service.get_model_type(CODE_QUERY) == ModelTypes.CODE.value


def test_search_query(chat_gpt_service):
    assert chat_gpt_service.search_query(SHORT_QUERY) == UNKNOWN
