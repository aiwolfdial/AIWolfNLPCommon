from aiwolf_nlp_common.protocol.map.remain_talk_map import RemainTalkMap, AgentRemainTalk


def test_set_received_info(initialize_json:dict) -> None:
    test_map = RemainTalkMap()
    test_map.set_received_info(set_map=initialize_json["gameInfo"]["remainTalkMap"])

    check_set:set[AgentRemainTalk] = set()

    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"
        add_elem = AgentRemainTalk(agent=name, remain_talk_number=5)
        check_set.add(add_elem)

    assert test_map == check_set