from __future__ import annotations

import json

from .info.info import Info
from .list import TalkList, WhisperList
from .setting.setting import Setting


class CommunicationProtocol:
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
    def initialize_from_json(cls, value: str) -> CommunicationProtocol:
        received_json: dict = json.loads(value)
        return cls(
            received_json["request"],
            (
                Info.initialize_from_json(value=received_json["info"])
                if received_json.get("info")
                else None
            ),
            (
                Setting.initialize_from_json(value=received_json["setting"])
                if received_json.get("setting")
                else None
            ),
            TalkList(value=received_json.get("talkHistory")),
            WhisperList(value=received_json.get("whisperHistory")),
        )

    def update_from_json(  # noqa: C901
        self,
        value: str,
    ) -> None:
        received_json: dict = json.loads(value)
        self.request = received_json["request"]
        if received_json.get("info") is not None:
            if self.is_info_empty():
                self.info = Info.initialize_from_json(value=received_json["info"])
            elif self.info is not None:
                self.info.update_from_json(value=received_json.get("info"))
        if received_json.get("setting") is not None:
            if self.is_setting_empty():
                self.setting = Setting.initialize_from_json(
                    value=received_json["setting"],
                )
            elif self.setting is not None:
                self.setting.update_from_json(value=received_json.get("setting"))
        if received_json.get("talkHistory") is not None:
            self.talk_history = TalkList(value=received_json.get("talkHistory"))
        elif self.talk_history is not None:
            self.talk_history.clear()
        if received_json.get("whisperHistory") is not None:
            self.whisper_history = WhisperList(
                value=received_json.get("whisperHistory"),
            )
        elif self.whisper_history is not None:
            self.whisper_history.clear()

    def is_info_empty(self) -> bool:
        return self.info is None

    def is_setting_empty(self) -> bool:
        return self.setting is None

    def is_talk_history_empty(self) -> bool:
        return self.talk_history is None

    def is_whisper_history_empty(self) -> bool:
        return self.whisper_history is None
