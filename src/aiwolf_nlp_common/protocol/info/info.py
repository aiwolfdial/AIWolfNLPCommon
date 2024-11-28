from __future__ import annotations

from aiwolf_nlp_common.protocol.info.result import DivineResult, MediumResult

from .list import AttackVoteList, VoteList
from .map.role_map import RoleMap
from .map.status_map import StatusMap


class Info:
    day: int
    agent: str
    medium_result: MediumResult
    divine_result: DivineResult
    executed_agent: str | None
    attacked_agent: str | None
    vote_list: VoteList
    attack_vote_list: AttackVoteList
    status_map: StatusMap
    role_map: RoleMap

    def __str__(self) -> str:
        executed_text = (
            self.executed_agent if self.has_executed_agent() else "No Result Available"
        )
        attacked_text = (
            self.attacked_agent if self.has_attacked_agent() else "No Result Available"
        )

        return (
            f"Day: {self.day}\n"
            f"Agent: {self.agent}\n\n"
            f"{self.medium_result}\n\n"
            f"{self.divine_result}\n\n"
            f"Executed Agent: {executed_text}\n"
            f"Attacked Agent: {attacked_text}\n\n"
            f"{self.status_map}\n\n"
            f"{self.role_map}\n\n"
        )

    def __init__(self, value: dict | None = None) -> None:
        if value is not None:
            self.day = value["day"]
            self.agent = value["agent"]
            self.medium_result = MediumResult(value.get("mediumResult"))
            self.divine_result = DivineResult(value.get("divineResult"))
            self.executed_agent = value.get("executedAgent")
            self.attacked_agent = value.get("attackedAgent")
            self.vote_list = VoteList(value.get("voteList"))
            self.attack_vote_list = AttackVoteList(value.get("attackVoteList"))
            self.status_map = StatusMap(value["statusMap"])
            self.role_map = RoleMap(value["roleMap"])

    def update(self, value: dict | None) -> None:
        self.__init__(value)

    def has_executed_agent(self) -> bool:
        return self.executed_agent is not None

    def has_attacked_agent(self) -> bool:
        return self.attacked_agent is not None
