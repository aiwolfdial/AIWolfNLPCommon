from .gameInfo.game_info import GameInfo
from .gameSetting.game_setting import GameSetting
import json


class CommunicationProtocol:
    game_info: GameInfo
    game_setting: GameSetting

    def __init__(self, game_info: GameInfo, game_setting: GameSetting) -> None:
        self.game_info = game_info
        self.game_setting = game_setting

    @classmethod
    def initialize_from_json(cls, received_str: str) -> "CommunicationProtocol":
        received_json: dict = json.loads(received_str)
        return cls(
            GameInfo.initialize_from_json(value=received_json["gameInfo"]),
            GameSetting.initialize_from_json(value=received_json["gameSetting"]),
        )