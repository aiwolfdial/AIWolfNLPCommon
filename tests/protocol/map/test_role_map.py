from aiwolf_nlp_common.protocol.gameInfo.map.role_map import RoleMap, AgentRole
from aiwolf_nlp_common.role.role import AIWolfNLPRoleInfo


def test_set_received_info(initialize_json:dict, status_map_json:dict) -> None:
    test_map = RoleMap()
    test_map.set_received_info(set_map=initialize_json["gameInfo"]["roleMap"])

    check_set = set()
    check_set.add(AgentRole(agent="Agent[01]", role="VILLAGER"))

    assert test_map == check_set

    test_map.set_received_info(set_map=status_map_json["gameInfo"]["roleMap"])
    check_set.clear()
    check_set.add(AgentRole(agent="Agent[04]", role="WEREWOLF"))

    assert test_map == check_set