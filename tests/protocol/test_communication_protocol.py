from aiwolf_nlp_common.protocol.communication_protocol import CommunicationProtocol
from aiwolf_nlp_common.protocol.gameSetting.map.role_num_map import RoleNumInfo, RoleNumMap

def test_game_setting(initialize_str:str, initialize_json:dict) -> None:
    result = CommunicationProtocol.initialize_from_json(received_str=initialize_str)

    check_role_num_map = RoleNumMap()

    for role in initialize_json["gameSetting"]["roleNumMap"].keys():
        add_elem = RoleNumInfo(role=role, allocated_count=initialize_json["gameSetting"]["roleNumMap"][role])
        check_role_num_map.add(add_elem)

    assert result.game_setting.role_num_map == check_role_num_map
    assert result.game_setting.max_talk == initialize_json["gameSetting"]["maxTalk"]
    assert result.game_setting.action_timeout == initialize_json["gameSetting"]["actionTimeout"]