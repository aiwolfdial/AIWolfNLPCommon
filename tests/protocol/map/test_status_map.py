from aiwolf_nlp_common.protocol.map.status_map import StatusMap, Status


def test_set_received_info(initialize_json:dict, status_map_json:dict) -> None:
    test_map = StatusMap()
    test_map.set_received_info(set_map=initialize_json["gameInfo"]["statusMap"])

    check_dict = dict()
    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"
        check_dict[name] = Status.ALIVE

    assert test_map == check_dict

    test_map.set_received_info(set_map=status_map_json["gameInfo"]["statusMap"])
    check_dict.clear()

    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"
        check_dict[name] = Status.ALIVE
    
    check_dict["Agent[01]"] = check_dict["Agent[02]"] = check_dict["Agent[03]"] = Status.DEAD

    assert test_map == check_dict