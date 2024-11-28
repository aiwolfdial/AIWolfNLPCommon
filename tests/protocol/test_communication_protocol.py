from aiwolf_nlp_common.protocol.communication_protocol import CommunicationProtocol
from aiwolf_nlp_common.protocol.gameSetting.map.role_num_map import (
    RoleNumInfo,
    RoleNumMap,
)


def test_request(
    name_str: str, name_json: dict, initialize_str: str, initialize_json: dict
):
    test_protocol = CommunicationProtocol.initialize_from_json(value=name_str)

    assert test_protocol.request == name_json["request"]

    test_protocol = CommunicationProtocol.initialize_from_json(value=initialize_str)

    assert test_protocol.request == initialize_json["request"]


def test_game_info(initialize_str: str, initialize_json: dict) -> None:
    test_protocol = CommunicationProtocol.initialize_from_json(value=initialize_str)

    assert test_protocol.game_info.day == initialize_json["gameInfo"]["day"]
    assert test_protocol.game_info.agent == initialize_json["gameInfo"]["agent"]


def test_game_setting(initialize_str: str, initialize_json: dict) -> None:
    result = CommunicationProtocol.initialize_from_json(value=initialize_str)

    check_role_num_map = RoleNumMap()

    for role in initialize_json["gameSetting"]["roleNumMap"].keys():
        add_elem = RoleNumInfo(
            role=role,
            allocated_count=initialize_json["gameSetting"]["roleNumMap"][role],
        )
        check_role_num_map.add(add_elem)

    assert result.game_setting.role_num_map == check_role_num_map
    assert result.game_setting.max_talk == initialize_json["gameSetting"]["maxTalk"]
    assert (
        result.game_setting.action_timeout
        == initialize_json["gameSetting"]["actionTimeout"]
    )
