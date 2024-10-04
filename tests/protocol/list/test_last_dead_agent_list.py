from aiwolf_nlp_common.protocol.list.last_dead_agent_list import LastDeadAgentList

def test_set_received_info(initialize_json:dict, last_dead_agent_list_json:dict) -> None:
    test_list = LastDeadAgentList()
    test_list.set_received_info(set_list=initialize_json["gameInfo"]["lastDeadAgentList"])

    assert test_list == []

    test_list.set_received_info(set_list=last_dead_agent_list_json["gameInfo"]["lastDeadAgentList"])
    result:list = ["Agent[02]"]

    assert len(test_list) == len(result)
    assert all(x == y and type(x) == type(y) for x, y in zip(test_list, result))