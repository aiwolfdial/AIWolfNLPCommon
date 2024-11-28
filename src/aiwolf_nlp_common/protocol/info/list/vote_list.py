from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VoteInfo:
    agent: int
    day: int
    target: int

    def __str__(self) -> str:
        return f"Day {self.day}: {self.agent} -> {self.target}"


class VoteList(list[VoteInfo]):
    def __str__(self) -> str:
        output: str = f"[{self.__class__.__name__}]"
        return (
            f"{output}\nNo Result Available"
            if self.is_empty()
            else f"{output}\n" + "\n".join(map(str, self))
        )

    @classmethod
    def initialize_from_json(cls, value: list[dict] | None = None) -> VoteList:
        instance = cls()
        if value is None:
            return instance
        instance.extend(
            VoteInfo(
                agent=vote_info["agent"],
                day=vote_info["day"],
                target=vote_info["target"],
            )
            for vote_info in value
        )
        return instance

    def __init__(self, value: list[dict] | None = None) -> None:
        self.initialize_from_json(value)

    def is_empty(self) -> bool:
        return not bool(self)
