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
from .list import TalkList, WhisperList
from .setting.setting import Setting


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
    whisper_history: WhisperList | None

    def __init__(
        self,
        request: str,
        info: Info | None,
        setting: Setting | None,
        talk_history: TalkList | None,
        whisper_history: WhisperList | None,
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

    def __str__(self) -> str:
        return (
            f"Request: {self.request}\n\n"
            f"---info---\n"
            f"{self.info}\n"
            f"---setting---\n"
            f"{self.setting}\n"
            f"---talkHistory---\n"
            f"{self.talk_history}\n\n"
            f"---whisperHistory---\n"
            f"{self.whisper_history}\n"
        )

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
            TalkList.initialize_from_json(set_list=received_json.get("talkHistory")),
            WhisperList.initialize_from_json(set_list=received_json.get("whisperHistory")),
        )

    def update_from_json(self, received_str: str) -> CommunicationProtocol:
        received_json: dict = json.loads(received_str)

        self.request = received_json["request"]

        if received_json.get("info") is not None:
            if self.is_info_empty():
                self.info = Info.initialize_from_json(value=received_json["info"])
            else:
                self.info.update_from_json(value=received_json.get("info"))

        if received_json.get("setting") is not None:
            if self.is_setting_empty():
                self.setting = Setting.initialize_from_json(value=received_json["setting"])
            else:
                self.setting.update_from_json(value=received_json.get("setting"))

        if received_json.get("talkHistory") is not None:
            self.talk_history = TalkList.initialize_from_json(
                set_list=received_json.get("talkHistory")
            )
        else:
            self.talk_history.clear()

        if received_json.get("whisperHistory") is not None:
            self.whisper_history = WhisperList.initialize_from_json(
                set_list=received_json.get("whisperHistory")
            )
        else:
            self.whisper_history.clear()

    def is_info_empty(self) -> bool:
        return self.info is None

    def is_setting_empty(self) -> bool:
        return self.setting is None

    def is_talk_history_empty(self) -> bool:
        return self.talk_history is None

    def is_whisper_hisotry_empty(self) -> bool:
        return self.whisper_history is None
