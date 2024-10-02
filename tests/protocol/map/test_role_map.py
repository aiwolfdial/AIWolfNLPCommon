from aiwolf_nlp_common.protocol.map.role_map import RoleMap
from aiwolf_nlp_common.role.role import AIWolfNLPRoleInfo


def test_set_received_info(initialize_json:dict, status_map_json:dict) -> None:
    test_map = RoleMap()
    test_map.set_received_info(set_map=initialize_json["gameInfo"]["roleMap"])

    check_dict = dict()
    check_dict["Agent[01]"] = AIWolfNLPRoleInfo.VILLAGER

    assert test_map == check_dict

    test_map.set_received_info(set_map=status_map_json["gameInfo"]["roleMap"])
    check_dict.clear()
    check_dict["Agent[04]"] = AIWolfNLPRoleInfo.WEREWOLF

    assert test_map == check_dict
