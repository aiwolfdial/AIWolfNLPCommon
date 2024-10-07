from gameSetting.game_setting import GameSetting
from gameSetting.map.role_num_map import RoleNumMap


class CommunicationProtocol:
    game_setting: GameSetting

    def __init__(self, game_setting: GameSetting) -> None:
        self.game_setting = game_setting

    @staticmethod
    def object_hook(value: object) -> "CommunicationProtocol":
        return CommunicationProtocol(game_setting=value["gameSetting"])

    @staticmethod
    def json_decode(value: dict):
        if not isinstance(value, dict):
            return value

        if value["class"] == "gameSetting":
            return GameSetting.object_hook(value=value)
        if value["class"] == "RoleNumMap":
            return RoleNumMap.object_hook(value=value)

        return value
