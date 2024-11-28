from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TalkInfo:
    agent: str
    day: int
    idx: int
    text: str
    turn: str
    skip: bool
    over: bool

    def __str__(self) -> str:
        return f"index:{self.idx}, {self.agent}: {self.text}"

    def is_skip(self) -> bool:
        return self.skip

    def is_over(self) -> bool:
        return self.over

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TalkInfo):
            return False
        return (
            self.agent == other.agent
            and self.day == other.day
            and self.idx == other.idx
            and self.text == other.text
            and self.turn == other.turn
            and self.skip == other.skip
            and self.over == other.over
        )


class TalkList(list[TalkInfo]):
    def __str__(self) -> str:
        header = f"[{self.__class__.__name__}]"
        return (
            f"{header}\nNo Result Available"
            if self.is_empty()
            else f"{header}" + "\n".join(str(elem) for elem in self)
        )

    @classmethod
    def initialize_from_json(cls, value: list[dict] | None) -> TalkList:
        instance = cls()
        if not value:
            return instance
        instance.extend(
            TalkInfo(
                agent=talk_info["agent"],
                day=talk_info["day"],
                idx=talk_info["idx"],
                text=talk_info["text"],
                turn=talk_info["turn"],
                skip=talk_info["skip"],
                over=talk_info["over"],
            )
            for talk_info in value
        )
        return instance

    def __init__(self, value: list[dict] | None = None) -> None:
        self.initialize_from_json(value)

    def is_empty(self) -> bool:
        return not bool(self)
