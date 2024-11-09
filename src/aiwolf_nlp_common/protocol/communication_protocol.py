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

from .info.info import Info
from .setting.setting import Setting
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
        info (info | None): An instance of info containing the current
            state of the game, or None if not provided.
        setting (setting | None): An instance of setting containing the
            settings for the game, or None if not provided.
        talk_history (TalkList | None): A list of previous talks during the game, or
            None if not provided.
        whisper_history (TalkList | None): A list of previous whispers during the
            game, or None if not provided.
    """

    request: str
    info: Info | None
    setting: Setting | None
    talk_history: TalkList | None
    whisper_history: TalkList | None

    def __init__(
        self,
        request: str,
        info: Info | None,
        setting: Setting | None,
        talk_history: TalkList | None,
        whisper_history: TalkList | None,
    ) -> None:
        """Initialize a CommunicationProtocol instance.

        This docstring was created by a generative AI.

        Args:
            request (str): The type of request being made to the game server.
            info (info | None): The current state of the game.
            setting (setting | None): The settings for the game.
            talk_history (TalkList | None): The history of talks during the game.
            whisper_history (TalkList | None): The history of whispers during the game.
        """
        self.request = request
        self.info = info
        self.setting = setting
        self.talk_history = talk_history
        self.whisper_history = whisper_history

    @classmethod
    def initialize_from_json(cls, received_str: str) -> CommunicationProtocol:
        """Initializes a CommunicationProtocol instance from a JSON string.

        This docstring was created by a generative AI.
        This method parses the received JSON string to extract the relevant information
        and initializes a new instance of CommunicationProtocol with it. It looks for
        keys such as "request", "info", "setting", "talkList", and
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
            Info.initialize_from_json(value=received_json["info"])
            if received_json.get("info")
            else None,
            Setting.initialize_from_json(value=received_json["setting"])
            if received_json.get("setting")
            else None,
            TalkList.initialize_from_json(set_list=received_json.get("talkList")),
            TalkList.initialize_from_json(set_list=received_json.get("whisperList")),
        )
    
    def update_from_json(self, received_str: str) -> CommunicationProtocol:
        received_json: dict = json.loads(received_str)

        self.request = received_json["request"]

        if received_json.get("info") is not None:
            if not self.is_set_info():
                self.info = Info.initialize_from_json(value=received_json["info"])
            else:
                self.info.update_from_json(value=received_json.get("info"))
        
        if received_json.get("setting") is not None:
            if not self.is_set_setting():
                self.setting = Setting.initialize_from_json(value=received_json["setting"])
            else:
                self.setting.update_from_json(value=received_json.get("setting"))
        
        self.talk_history = TalkList.initialize_from_json(set_list=received_json.get("talkList"))
        self.whisper_history = TalkList.initialize_from_json(set_list=received_json.get("whisperList"))
    
    def is_set_info(self) -> bool:
        return not self.info is None
    
    def is_set_setting(self) -> bool:
        return not self.setting is None