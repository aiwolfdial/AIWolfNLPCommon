from __future__ import annotations

from .talk_list import TalkList


class WhisperList(TalkList):
    def __init__(self, whisper_list: list[dict] | None = None) -> None:
        super().__init__(whisper_list)
