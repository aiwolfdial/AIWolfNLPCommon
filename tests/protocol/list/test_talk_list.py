from aiwolf_nlp_common.protocol.list.talk_list import TalkInfo, TalkList

def test_set_received_info(initialize_json:dict, talk_list_json:dict) -> None:
    talk_list = TalkList()
    talk_list.set_received_info(set_list=initialize_json["gameInfo"]["talkList"])

    assert talk_list == []

    talk_list.set_received_info(set_list=talk_list_json["gameInfo"]["talkList"])
    result:list[TalkInfo] = []

    for temp in talk_list_json["gameInfo"]["talkList"]:
        add_elem =TalkInfo(agent=temp["agent"], day=temp["day"], idx=temp["idx"], text=temp["text"], turn=temp["turn"], skip=temp["skip"], over=temp["over"])
        result.append(add_elem)

    assert len(talk_list) == len(result)
    assert all(x == y and type(x) == type(y) for x, y in zip(talk_list, result))