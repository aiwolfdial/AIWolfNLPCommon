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
    - TalkList: A list extension class for storing talk and whisper information.
    - VoteList: A list extension class for storing vote information.
    - RemainTalkMap: A map class that stores the remaining talk counts for agents.
    - RoleMap: A map class that stores the roles of agents.
    - StatusMap: A map class that stores the status of agents.

The `info` class provides methods for initializing itself from JSON data and
storing various elements of the game state in its attributes.
"""

from __future__ import annotations

from aiwolf_nlp_common.protocol.talk_list import TalkList

from aiwolf_nlp_common.protocol.judgement_result import JudgementResult
from .list.vote_list import VoteList
from .map.remain_talk_map import RemainTalkMap
from .map.role_map import RoleMap
from .map.status_map import StatusMap


class Info:
    """Represents the current state of the game.
    TODO

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
        talk_list (TalkList): A list of all talks made during the game.
        whisper_list (TalkList): A list of whispers made during the game.
        status_map (StatusMap): A mapping of agent statuses (e.g., alive, dead).
        role_map (RoleMap): A mapping of agent roles.
        remain_talk_map (RemainTalkMap): A mapping of remaining talk counts for each agent.
        remain_whisper_map (RemainTalkMap): A mapping of remaining whisper counts for each agent.

    Methods:
        __init__(day, agent, vote_list, latest_vote_list, attack_vote_list,
                 latest_attack_vote_list, talk_list, whisper_list, status_map,
                 role_map, remain_talk_map, remain_whisper_map,
                 existing_role_list):
            Initializes a info instance with all game state information.

        initialize_from_json(value: dict) -> "info":
            Class method that initializes a info instance from JSON data received
            from the game server.
    """

    day: int
    agent: str
    medium_result: JudgementResult
    divine_result: JudgementResult
    executed_agent: str | None
    attacked_agent: str | None
    vote_list: VoteList
    attack_vote_list: VoteList
    talk_list: TalkList
    whisper_list: TalkList
    status_map: StatusMap
    role_map: RoleMap
    remain_talk_map: RemainTalkMap
    remain_whisper_map: RemainTalkMap

    def __init__(
        self,
        day: int,
        agent: str,
        medium_result: JudgementResult,
        divine_result: JudgementResult,
        executed_agent: str | None,
        attacked_agent: str | None,
        vote_list: VoteList,
        attack_vote_list: VoteList,
        talk_list: TalkList,
        whisper_list: TalkList,
        status_map: StatusMap,
        role_map: RoleMap,
        remain_talk_map: RemainTalkMap,
        remain_whisper_map: RemainTalkMap,
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
            talk_list (TalkList): List of talks made during the game.
            whisper_list (TalkList): List of whispers made during the game.
            status_map (StatusMap): Map of player statuses.
            role_map (RoleMap): Map of player roles.
            remain_talk_map (RemainTalkMap): Map of remaining talks for each player.
            remain_whisper_map (RemainTalkMap): Map of remaining whispers for each player.
        """
        self.day = day
        self.agent = agent
        self.medium_result = medium_result
        self.divine_result = divine_result
        self.executed_agent = executed_agent
        self.attacked_agent = attacked_agent
        self.vote_list = vote_list
        self.attack_vote_list = attack_vote_list
        self.talk_list = talk_list
        self.whisper_list = whisper_list
        self.status_map = status_map
        self.role_map = role_map
        self.remain_talk_map = remain_talk_map
        self.remain_whisper_map = remain_whisper_map

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
                - "talkList" (list): The list of talks made by agents.
                - "whisperList" (list): The list of whispers made by agents.
                - "statusMap" (dict): The current status of agents.
                - "roleMap" (dict): The roles assigned to agents.
                - "remainTalkMap" (dict): The remaining talk counts for agents.
                - "remainWhisperMap" (dict): The remaining whisper counts for agents.

        Returns:
            info: An instance of info initialized with the provided JSON data.
        """
        return cls(
            day=value["day"],
            agent=value["agent"],
            medium_result=JudgementResult.initialize_from_json(
                value=value.get("mediumResult", None)
            ),
            divine_result=JudgementResult.initialize_from_json(
                value=value.get("divineResult", None)
            ),
            executed_agent=value.get("executedAgent", None),
            attacked_agent=value.get("attackedAgent", None),
            vote_list=VoteList.initialize_from_json(value.get("voteList", None)),
            attack_vote_list=VoteList.initialize_from_json(value.get("attackVoteList", None)),
            talk_list=TalkList.initialize_from_json(value.get("talkList", None)),
            whisper_list=TalkList.initialize_from_json(value.get("whisperList", None)),
            status_map=StatusMap.initialize_from_json(value["statusMap"]),
            role_map=RoleMap.initialize_from_json(value["roleMap"]),
            remain_talk_map=RemainTalkMap.initialize_from_json(value["remainTalkMap"]),
            remain_whisper_map=RemainTalkMap.initialize_from_json(value["remainWhisperMap"]),
        )
    
    def update_from_json(self, value: dict | None) -> None:

        if value is None:
            return None
        
        self.day = value["day"]
        self.agent = value["agent"]
        self.medium_result = JudgementResult.initialize_from_json(value.get("mediumResult", None))
        self.divine_result = JudgementResult.initialize_from_json(value.get("divineResult", None))
        self.executed_agent = value.get("executedAgent", None)
        self.attacked_agent = value.get("attackedAgent", None)
        self.vote_list.initialize_from_json(value.get("voteList", None))
        self.attack_vote_list.initialize_from_json(value.get("attackVoteList", None))
        self.talk_list.initialize_from_json(value.get("talkList", None))
        self.whisper_list.initialize_from_json(value.get("whisperList", None))
        self.status_map=StatusMap.initialize_from_json(value["statusMap"])
        self.role_map=RoleMap.initialize_from_json(value["roleMap"])
        self.remain_talk_map=RemainTalkMap.initialize_from_json(value["remainTalkMap"])
        self.remain_whisper_map=RemainTalkMap.initialize_from_json(value["remainWhisperMap"])

    def has_executed_agent(self) -> bool:
        return self.executed_agent is not None

    def has_attacked_agent(self) -> bool:
        return self.attacked_agent is not None
