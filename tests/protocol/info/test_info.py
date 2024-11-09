from aiwolf_nlp_common.protocol.info import Info

def test_info(initialize_json):
    info = Info.initialize_from_json(value=initialize_json)
    info_key = "info"

    assert initialize_json[info_key]["day"] == info.day