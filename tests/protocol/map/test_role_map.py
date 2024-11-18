import pytest

from aiwolf_nlp_common.protocol.gameInfo.map.role_map import AgentRole, RoleMap
from aiwolf_nlp_common.role.role import RoleInfo


def test_set_received_info(initialize_json: dict, status_map_json: dict) -> None:
    test_map = RoleMap.initialize_from_json(set_map=initialize_json["gameInfo"]["roleMap"])

    check_set = set()
    check_set.add(AgentRole(agent="Agent[01]", role="VILLAGER"))

    assert test_map == check_set

    test_map = RoleMap.initialize_from_json(set_map=status_map_json["gameInfo"]["roleMap"])
    check_set.clear()
    check_set.add(AgentRole(agent="Agent[04]", role="WEREWOLF"))

    assert test_map == check_set


def test_get_agent_role(initialize_json: dict) -> None:
    test_map = RoleMap.initialize_from_json(set_map=initialize_json["gameInfo"]["roleMap"])

    assert test_map.get_agent_role(agent="Agent[01]") == RoleInfo.VILLAGER.value

    with pytest.raises(ValueError) as e:
        test_map.get_agent_role(agent="Agent[02]")
        test_map.get_agent_role(agent="Agent[03]")
        test_map.get_agent_role(agent="Agent[04]")
        test_map.get_agent_role(agent="Agent[05]")
