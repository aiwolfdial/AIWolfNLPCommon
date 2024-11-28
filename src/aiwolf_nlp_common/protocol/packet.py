from __future__ import annotations

from .info.info import Info
from .list import TalkList, WhisperList
from .setting.setting import Setting


class Packet:
    request: str
    info: Info | None
    setting: Setting | None
    talk_history: TalkList | None
    whisper_history: WhisperList | None

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

    def __init__(self, value: dict) -> None:
        self.request = value["request"]
        if value.get("info") is not None:
            self.info = Info(value=value.get("info"))
        else:
            self.info = None
        if value.get("setting") is not None:
            self.setting = Setting(value=value.get("setting"))
        else:
            self.setting = None
        if value.get("talkHistory") is not None:
            self.talk_history = TalkList(value=value.get("talkHistory"))
        else:
            self.talk_history = None
        if value.get("whisperHistory") is not None:
            self.whisper_history = WhisperList(value=value.get("whisperHistory"))
        else:
            self.whisper_history = None

    def update(
        self,
        value: dict,
    ) -> None:
        self.request = value["request"]
        if value.get("info") is not None:
            if self.info is None:
                self.info = Info(value=value["info"])
            else:
                self.info.update(value=value.get("info"))
        if value.get("setting") is not None:
            if self.setting is None:
                self.setting = Setting(
                    value=value["setting"],
                )
            else:
                self.setting.update(value=value.get("setting"))
        if value.get("talkHistory") is not None:
            self.talk_history = TalkList(value=value.get("talkHistory"))
        elif self.talk_history is not None:
            self.talk_history.clear()
        if value.get("whisperHistory") is not None:
            self.whisper_history = WhisperList(
                value=value.get("whisperHistory"),
            )
        elif self.whisper_history is not None:
            self.whisper_history.clear()
