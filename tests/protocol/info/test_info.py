from aiwolf_nlp_common.protocol.info import Info
from aiwolf_nlp_common.role import RoleInfo


def test_info(initialize_json):
    info_key = "info"
    info = Info.initialize_from_json(value=initialize_json[info_key])

    assert initialize_json[info_key]["day"] == info.day
    assert initialize_json[info_key]["agent"] == info.agent
    assert info.medium_result.is_empty()
    assert not info.has_executed_agent()
    assert not info.has_attacked_agent()
    assert info.vote_list.is_empty()
    assert info.attack_vote_list.is_empty()
    assert info.status_map.get_alive_agent_list() == [
        "Agent[01]",
        "Agent[02]",
        "Agent[03]",
        "Agent[04]",
        "Agent[05]",
    ]
    assert info.role_map.get_role(agent="Agent[01]") == RoleInfo.VILLAGER.value
