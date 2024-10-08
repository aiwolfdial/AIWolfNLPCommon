"""Initialize a CommunicationProtocol instance from a JSON string.

This docstring was created by a generative AI.
This module defines the CommunicationProtocol class, which manages communication
between the game server and the client. It facilitates the handling of requests,
game information, game settings, and communication history.

Classes:
    CommunicationProtocol: A class that encapsulates the communication protocol
    with the game server.
"""

from __future__ import annotations

import json

from .gameInfo.game_info import GameInfo
from .gameSetting.game_setting import GameSetting
from .talk_list import TalkList


class CommunicationProtocol:
    """Class representing the communication protocol with the game server.

    This docstring was created by a generative AI.
    This class manages the data exchanged between the client and the game server,
    including the request type, game information, game settings, and the history of
    talks and whispers. It provides methods for initializing its state from JSON data
    received from the server.

    Attributes:
        request (str): The type of request being made to the game server.
        game_info (GameInfo | None): An instance of GameInfo containing the current
            state of the game, or None if not provided.
        game_setting (GameSetting | None): An instance of GameSetting containing the
            settings for the game, or None if not provided.
        talk_history (TalkList | None): A list of previous talks during the game, or
            None if not provided.
        whisper_history (TalkList | None): A list of previous whispers during the
            game, or None if not provided.
    """

    request: str
    game_info: GameInfo | None
    game_setting: GameSetting | None
    talk_history: TalkList | None
    whisper_history: TalkList | None

    def __init__(
        self,
        request: str,
        game_info: GameInfo | None,
        game_setting: GameSetting | None,
        talk_history: TalkList | None,
        whisper_history: TalkList | None,
    ) -> None:
        """Initialize a CommunicationProtocol instance.

        This docstring was created by a generative AI.

        Args:
            request (str): The type of request being made to the game server.
            game_info (GameInfo | None): The current state of the game.
            game_setting (GameSetting | None): The settings for the game.
            talk_history (TalkList | None): The history of talks during the game.
            whisper_history (TalkList | None): The history of whispers during the game.
        """
        self.request = request
        self.game_info = game_info
        self.game_setting = game_setting
        self.talk_history = talk_history
        self.whisper_history = whisper_history

    @classmethod
    def initialize_from_json(cls, received_str: str) -> CommunicationProtocol:
        """Initializes a CommunicationProtocol instance from a JSON string.

        This docstring was created by a generative AI.
        This method parses the received JSON string to extract the relevant information
        and initializes a new instance of CommunicationProtocol with it. It looks for
        keys such as "request", "gameInfo", "gameSetting", "talkList", and
        "whisperList" to populate the instance attributes.

        Args:
            received_str (str): A JSON string received from the game server, which
                contains the request and other game-related data.

        Returns:
            CommunicationProtocol: An instance of CommunicationProtocol initialized
            with the parsed data from the JSON string.
        """
        received_json: dict = json.loads(received_str)
        return cls(
            received_json["request"],
            GameInfo.initialize_from_json(value=received_json["gameInfo"])
            if received_json.get("gameInfo")
            else None,
            GameSetting.initialize_from_json(value=received_json["gameSetting"])
            if received_json.get("gameSetting")
            else None,
            TalkList.initialize_from_json(set_list=received_json["talkList"])
            if received_json.get("talkList")
            else None,
            TalkList.initialize_from_json(set_list=received_json["whisperList"])
            if received_json.get("whisperList")
            else None,
        )
