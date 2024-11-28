from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class JudgementResult:
    DEFAULT_DAY: ClassVar[int] = -1
    DEFAULT_AGENT: ClassVar[str] = "Agent[00]"
    DEFAULT_TARGET: ClassVar[str] = "Agent[00]"
    DEFAULT_RESULT: ClassVar[str] = "unknown"

    day: int = DEFAULT_DAY
    agent: str = DEFAULT_AGENT
    target: str = DEFAULT_TARGET
    result: str = DEFAULT_RESULT

    def __str__(self) -> str:
        if self.is_empty():
            return f"[{self.__class__.__name__}]\nNo Result Available"
        return f"[{self.__class__.__name__}]\nDay {self.day} : {self.target} is {self.result}"

    @classmethod
    def initialize_from_json(cls, value: dict | None) -> JudgementResult:
        if value is None:
            return cls()
        return cls(**value)

    def __init__(self, value: dict | None = None) -> None:
        self.initialize_from_json(value)

    def reset(self) -> None:
        self.day = self.DEFAULT_DAY
        self.agent = self.DEFAULT_AGENT
        self.target = self.DEFAULT_TARGET
        self.result = self.DEFAULT_RESULT

    def is_empty(self) -> bool:
        return (
            self.day == self.DEFAULT_DAY
            and self.agent == self.DEFAULT_AGENT
            and self.target == self.DEFAULT_TARGET
            and self.result == self.DEFAULT_RESULT
        )
