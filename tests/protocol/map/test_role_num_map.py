import pytest

from aiwolf_nlp_common.protocol.gameInfo.map.role_map import AgentRole, RoleMap
from aiwolf_nlp_common.protocol.gameSetting.map.role_num_map import RoleNumMap
from aiwolf_nlp_common.role.role import RoleInfo


def test_get_agent_list(initialize_json: dict) -> None:
    test_map = RoleNumMap(value=initialize_json["gameSetting"]["roleNumMap"])

    assert test_map.get_role_num(role=RoleInfo.VILLAGER.value) == 2
    assert test_map.get_role_num(role="SEER") == 1
    assert test_map.get_role_num(role=RoleInfo.WEREWOLF) == 1

    with pytest.raises(ValueError) as e:
        test_map.get_role_num(role="Seer")
