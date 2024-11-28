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

    def __init__(self, value: list[dict] | None = None) -> None:
        super().__init__()
        if value is not None:
            self.extend(
                VoteInfo(
                    agent=vote_info["agent"],
                    day=vote_info["day"],
                    target=vote_info["target"],
                )
                for vote_info in value
            )

    def is_empty(self) -> bool:
        return not bool(self)
