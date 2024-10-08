import pytest
from aiwolf_nlp_common.protocol.gameSetting.map.role_num_map import RoleNumMap
from aiwolf_nlp_common.protocol.gameInfo.map.role_map import RoleMap, AgentRole
from aiwolf_nlp_common.role.role import RoleInfo

def test_get_agent_list(initialize_json:dict) -> None:
    test_map = RoleNumMap.initialize_from_json(value=initialize_json["gameSetting"]["roleNumMap"])

    assert test_map.get_role_num(role=RoleInfo.VILLAGER.value) == 2
    assert test_map.get_role_num(role="SEER") == 1