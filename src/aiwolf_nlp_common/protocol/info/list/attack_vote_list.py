from __future__ import annotations

from .vote_list import VoteList


class AttackVoteList(VoteList):
    def __init__(self, value: list[dict] | None = None) -> None:
        super().__init__(value)
