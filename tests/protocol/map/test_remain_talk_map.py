from aiwolf_nlp_common.protocol.gameInfo.map.remain_talk_map import RemainTalkMap, AgentRemainTalkInfo


def test_set_received_info(initialize_json:dict) -> None:
    test_map = RemainTalkMap.initialize_from_json(set_map=initialize_json["gameInfo"]["remainTalkMap"])

    check_set:set[AgentRemainTalkInfo] = set()

    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"
        add_elem = AgentRemainTalkInfo(agent=name, remain_talk_number=5)
        check_set.add(add_elem)

    assert test_map == check_set

def test_talk_info_eq() -> None:
    
    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"
        elem1 = AgentRemainTalkInfo(agent=name, remain_talk_number=5)
        elem2 = AgentRemainTalkInfo(agent=name, remain_talk_number=5)
        elem3 = AgentRemainTalkInfo(agent=name+"]", remain_talk_number=5)
        elem4 = AgentRemainTalkInfo(agent=name, remain_talk_number=6)

        assert elem1 == elem2
        assert elem1 != elem3
        assert elem1 != elem4
        assert elem1 != None
        assert elem1 != i

def test_get_agent_remain_talk_number(initialize_json:dict) -> None:
    test_map = RemainTalkMap.initialize_from_json(set_map=initialize_json["gameInfo"]["remainTalkMap"])

    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"
        assert test_map.get_agent_remain_talk_number(agent=name) == 5