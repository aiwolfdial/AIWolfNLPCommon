from aiwolf_nlp_common.protocol.talk_list import TalkInfo, TalkList


def test_set_received_info(initialize_json: dict, talk_list_json: dict) -> None:
    talk_list = TalkList.initialize_from_json(set_list=initialize_json["gameInfo"]["talkList"])

    assert talk_list == []

    talk_list = TalkList.initialize_from_json(set_list=talk_list_json["gameInfo"]["talkList"])
    result: list[TalkInfo] = []

    for temp in talk_list_json["gameInfo"]["talkList"]:
        add_elem = TalkInfo(
            agent=temp["agent"],
            day=temp["day"],
            idx=temp["idx"],
            text=temp["text"],
            turn=temp["turn"],
            skip=temp["skip"],
            over=temp["over"],
        )
        result.append(add_elem)

    assert len(talk_list) == len(result)
    assert all(x == y and type(x) == type(y) for x, y in zip(talk_list, result))

    talk: TalkInfo
    for talk in talk_list:
        if talk.text == "Skip":
            assert talk.is_skip() and not talk.is_over()
        elif talk.text == "Over":
            assert not talk.is_skip() and talk.is_over()
        else:
            assert not talk.is_skip() and not talk.is_over()
