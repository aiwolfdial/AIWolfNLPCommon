from aiwolf_nlp_common.action import AIWolfNLPAction

def test_initialize(initialize_json) -> None:

    request = initialize_json["request"]

    assert AIWolfNLPAction.is_initialize(request=request)