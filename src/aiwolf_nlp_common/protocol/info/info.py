"""info Module.

This docstring was created by a generative AI.
This module defines the info class, which is responsible for storing and handling
the current state of a game based on data received from a game server. It includes
various attributes such as the current day, agent details, vote lists, talk lists,
role maps, status maps, and more. These attributes are initialized using JSON data
received from the game server.

Classes:
    info: A class that represents the game state, including the current day, agent
    information, votes, talks, roles, statuses, and other related game data.

Imported Modules:
    - VoteList: A list extension class for storing vote information.
    - RoleMap: A map class that stores the roles of agents.
    - StatusMap: A map class that stores the status of agents.

The `info` class provides methods for initializing itself from JSON data and
storing various elements of the game state in its attributes.
"""

from __future__ import annotations

from aiwolf_nlp_common.protocol.info.result import DivineResult, MediumResult

from .list import AttackVoteList, VoteList
from .map.role_map import RoleMap
from .map.status_map import StatusMap


class Info:
    """Represents the current state of the game.

    This docstring was created by a generative AI.
    The info class encapsulates all relevant information about the ongoing game, including
    the current day, the active agent, and various lists and maps that track votes, talks, roles,
    and agent statuses. This class provides a structured way to manage and access game data,
    facilitating interactions between game components.

    Attributes:
        day (int): The current day of the game.
        agent (str): The identifier of the current agent.
        medium_result (JudgementResult):
        divine_result: (JudgementResult):
        vote_list (VoteList): A list of votes that have been cast during the game.
        attack_vote_list (VoteList): A list of votes related to attacks.
        status_map (StatusMap): A mapping of agent statuses (e.g., alive, dead).
        role_map (RoleMap): A mapping of agent roles.

    Methods:
        __init__(day, agent, vote_list, latest_vote_list, attack_vote_list,
                 latest_attack_vote_list, status_map,
                 role_map,
                 existing_role_list):
            Initializes a info instance with all game state information.

        initialize_from_json(value: dict) -> "info":
            Class method that initializes a info instance from JSON data received
            from the game server.
    """

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

    def __init__(
        self,
        day: int,
        agent: str,
        medium_result: MediumResult,
        divine_result: DivineResult,
        executed_agent: str | None,
        attacked_agent: str | None,
        vote_list: VoteList,
        attack_vote_list: AttackVoteList,
        status_map: StatusMap,
        role_map: RoleMap,
    ) -> None:
        """Initialize a info instance with all game state information.

        This description was written by Claude 3.5 Sonnet.

        Args:
            day (int): The current day in the game.
            agent (str): The identifier of the current agent.
            medium_result (JudgementResult):
            divine_result: (JudgementResult):
            executed_agent: (str):
            vote_list (VoteList): List of votes cast.
            attack_vote_list (VoteList): List of attack votes.
            status_map (StatusMap): Map of player statuses.
            role_map (RoleMap): Map of player roles.
        """
        self.day = day
        self.agent = agent
        self.medium_result = medium_result
        self.divine_result = divine_result
        self.executed_agent = executed_agent
        self.attacked_agent = attacked_agent
        self.vote_list = vote_list
        self.attack_vote_list = attack_vote_list
        self.status_map = status_map
        self.role_map = role_map

    def __str__(self) -> str:
        return (
            f"Day: {self.day}\n"
            f"Agent: {self.agent}\n\n"
            f"{self.medium_result}\n\n"
            f"{self.divine_result}\n\n"
            f"Executed Agent: {self.executed_agent if self.has_executed_agent() else 'No Result Available'}\n"
            f"Attacked Agent: {self.attacked_agent if self.has_attacked_agent() else 'No Result Available'}\n\n"
            f"{self.status_map}\n\n"
            f"{self.role_map}\n\n"
        )

    @classmethod
    def initialize_from_json(cls, value: dict) -> Info:
        """Initializes a info instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method takes a dictionary containing information about the game state and
        initializes a new info instance with it. The provided JSON data is expected
        to include various components such as the current day, the agent's ID, and lists
        of votes, talks, and agent statuses, among others.

        Args:
            value (dict): JSON dictionary of "info" received from the game server.
                The expected structure includes:
                - "day" (int): The current day of the game.
                - "agent" (int): The ID of the agent.
                - "voteList" (list): The list of votes cast.
                - "attackVoteList" (list): The list of attack votes.
                - "statusMap" (dict): The current status of agents.
                - "roleMap" (dict): The roles assigned to agents.

        Returns:
            info: An instance of info initialized with the provided JSON data.
        """
        return cls(
            day=value["day"],
            agent=value["agent"],
            medium_result=MediumResult.initialize_from_json(value=value.get("mediumResult", None)),
            divine_result=DivineResult.initialize_from_json(value=value.get("divineResult", None)),
            executed_agent=value.get("executedAgent", None),
            attacked_agent=value.get("attackedAgent", None),
            vote_list=VoteList.initialize_from_json(value.get("voteList", None)),
            attack_vote_list=AttackVoteList.initialize_from_json(value.get("attackVoteList", None)),
            status_map=StatusMap.initialize_from_json(value["statusMap"]),
            role_map=RoleMap.initialize_from_json(value["roleMap"]),
        )

    def update_from_json(self, value: dict | None) -> None:
        if value is None:
            return None

        self.day = value["day"]
        self.agent = value["agent"]
        self.medium_result = MediumResult.initialize_from_json(value.get("mediumResult", None))
        self.divine_result = DivineResult.initialize_from_json(value.get("divineResult", None))
        self.executed_agent = value.get("executedAgent", None)
        self.attacked_agent = value.get("attackedAgent", None)
        self.vote_list = VoteList.initialize_from_json(value.get("voteList", None))
        self.attack_vote_list = AttackVoteList.initialize_from_json(
            value.get("attackVoteList", None)
        )
        self.status_map = StatusMap.initialize_from_json(value["statusMap"])
        self.role_map = RoleMap.initialize_from_json(value["roleMap"])

    def has_executed_agent(self) -> bool:
        return self.executed_agent is not None

    def has_attacked_agent(self) -> bool:
        return self.attacked_agent is not None
