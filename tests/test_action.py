from aiwolf_nlp_common.action import AIWolfNLPAction

def test_initialize(get_initialize_json) -> None:
    initialize_json: dict = get_initialize_json

    request = initialize_json["request"]

    assert AIWolfNLPAction.is_initialize(request=request)