from aiwolf_nlp_common.protocol.communication_protocol import CommunicationProtocol
from aiwolf_nlp_common.protocol.gameSetting.map.role_num_map import RoleNumInfo, RoleNumMap

def check_game_info(initialize_str:str, initialize_json:dict) -> None:
    test_protocol = CommunicationProtocol.initialize_from_json(received_str=initialize_str)

    assert test_protocol.game_info.day == initialize_json["gameInfo"]["day"]
    assert test_protocol.game_info.agent == initialize_json["gameInfo"]["agent"]

def check_game_setting(initialize_str:str, initialize_json:dict) -> None:
    result = CommunicationProtocol.initialize_from_json(received_str=initialize_str)

    check_role_num_map = RoleNumMap()

    for role in initialize_json["gameSetting"]["roleNumMap"].keys():
        add_elem = RoleNumInfo(role=role, allocated_count=initialize_json["gameSetting"]["roleNumMap"][role])
        check_role_num_map.add(add_elem)

    assert result.game_setting.role_num_map == check_role_num_map
    assert result.game_setting.max_talk == initialize_json["gameSetting"]["maxTalk"]
    assert result.game_setting.action_timeout == initialize_json["gameSetting"]["actionTimeout"]

def test_initialize_from_json(initialize_str:str, initialize_json:dict) -> None:
    check_game_info(initialize_str=initialize_str, initialize_json=initialize_json)
    check_game_setting(initialize_str=initialize_str, initialize_json=initialize_json)