from aiwolf_nlp_common.protocol.gameInfo.list.vote_list import VoteInfo, VoteList


def test_set_received_info(initialize_json: dict, vote_list_json: dict) -> None:
    vote_list = VoteList.initialize_from_json(set_list=initialize_json["gameInfo"]["voteList"])

    assert vote_list == []

    vote_list = VoteList.initialize_from_json(set_list=vote_list_json["gameInfo"]["voteList"])
    result: list[VoteInfo] = []

    for temp in vote_list_json["gameInfo"]["voteList"]:
        add_elem = VoteInfo(agent=temp["agent"], day=temp["day"], target=temp["target"])
        result.append(add_elem)

    assert len(vote_list) == len(result)
    assert all(x == y and type(x) == type(y) for x, y in zip(vote_list, result))
