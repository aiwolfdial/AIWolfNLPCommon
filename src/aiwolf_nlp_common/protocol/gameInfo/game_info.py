"""GameInfo Module.

This docstring was created by a generative AI.
This module defines the GameInfo class, which is responsible for storing and handling
the current state of a game based on data received from a game server. It includes
various attributes such as the current day, agent details, vote lists, talk lists,
role maps, status maps, and more. These attributes are initialized using JSON data
received from the game server.

Classes:
    GameInfo: A class that represents the game state, including the current day, agent
    information, votes, talks, roles, statuses, and other related game data.

Imported Modules:
    - ExistingRoleList: A list extension class for storing the roles that are present
      in the game.
    - LastDeadAgentList: A list extension class for storing the information of agents
      who died last.
    - TalkList: A list extension class for storing talk and whisper information.
    - VoteList: A list extension class for storing vote information.
    - RemainTalkMap: A map class that stores the remaining talk counts for agents.
    - RoleMap: A map class that stores the roles of agents.
    - StatusMap: A map class that stores the status of agents.

The `GameInfo` class provides methods for initializing itself from JSON data and
storing various elements of the game state in its attributes.
"""

from .list.existing_role_list import ExistingRoleList
from .list.last_dead_agent_list import LastDeadAgentList
from .list.talk_list import TalkList
from .list.vote_list import VoteList
from .map.remain_talk_map import RemainTalkMap
from .map.role_map import RoleMap
from .map.status_map import StatusMap


class GameInfo:
    """Represents the current state of the game.

    This docstring was created by a generative AI.
    The GameInfo class encapsulates all relevant information about the ongoing game, including
    the current day, the active agent, and various lists and maps that track votes, talks, roles,
    and agent statuses. This class provides a structured way to manage and access game data,
    facilitating interactions between game components.

    Attributes:
        day (int): The current day of the game.
        agent (str): The identifier of the current agent.
        vote_list (VoteList): A list of votes that have been cast during the game.
        latest_vote_list (VoteList): The most recent list of votes.
        attack_vote_list (VoteList): A list of votes related to attacks.
        latest_attack_vote_list (VoteList): The most recent list of attack votes.
        talk_list (TalkList): A list of all talks made during the game.
        whisper_list (TalkList): A list of whispers made during the game.
        status_map (StatusMap): A mapping of agent statuses (e.g., alive, dead).
        role_map (RoleMap): A mapping of agent roles.
        remain_talk_map (RemainTalkMap): A mapping of remaining talk counts for each agent.
        remain_whisper_map (RemainTalkMap): A mapping of remaining whisper counts for each agent.
        existing_role_list (ExistingRoleList): A list of roles currently in the game.
        last_dead_agent_list (LastDeadAgentList): A list of agents that have died.

    Methods:
        __init__(day, agent, vote_list, latest_vote_list, attack_vote_list,
                 latest_attack_vote_list, talk_list, whisper_list, status_map,
                 role_map, remain_talk_map, remain_whisper_map,
                 existing_role_list, last_dead_agent_list):
            Initializes a GameInfo instance with all game state information.

        initialize_from_json(value: dict) -> "GameInfo":
            Class method that initializes a GameInfo instance from JSON data received
            from the game server.
    """

    day: int
    agent: str
    vote_list: VoteList
    latest_vote_list: VoteList
    attack_vote_list: VoteList
    latest_attack_vote_list: VoteList
    talk_list: TalkList
    whisper_list: TalkList
    status_map: StatusMap
    role_map: RoleMap
    remain_talk_map: RemainTalkMap
    remain_whisper_map: RemainTalkMap
    existing_role_list: ExistingRoleList
    last_dead_agent_list: LastDeadAgentList

    def __init__(
        self,
        day: int,
        agent: str,
        vote_list: VoteList,
        latest_vote_list: VoteList,
        attack_vote_list: VoteList,
        latest_attack_vote_list: VoteList,
        talk_list: TalkList,
        whisper_list: TalkList,
        status_map: StatusMap,
        role_map: RoleMap,
        remain_talk_map: RemainTalkMap,
        remain_whisper_map: RemainTalkMap,
        existing_role_list: ExistingRoleList,
        last_dead_agent_list: LastDeadAgentList,
    ) -> None:
        """Initialize a GameInfo instance with all game state information.

        This description was written by Claude 3.5 Sonnet.

        Args:
            day (int): The current day in the game.
            agent (str): The identifier of the current agent.
            vote_list (VoteList): List of votes cast.
            latest_vote_list (VoteList): Most recent list of votes.
            attack_vote_list (VoteList): List of attack votes.
            latest_attack_vote_list (VoteList): Most recent list of attack votes.
            talk_list (TalkList): List of talks made during the game.
            whisper_list (TalkList): List of whispers made during the game.
            status_map (StatusMap): Map of player statuses.
            role_map (RoleMap): Map of player roles.
            remain_talk_map (RemainTalkMap): Map of remaining talks for each player.
            remain_whisper_map (RemainTalkMap): Map of remaining whispers for each player.
            existing_role_list (ExistingRoleList): List of roles currently in the game.
            last_dead_agent_list (LastDeadAgentList): List of agents who died last.
        """
        self.day = day
        self.agent = agent
        self.vote_list = vote_list
        self.latest_vote_list = latest_vote_list
        self.attack_vote_list = attack_vote_list
        self.latest_attack_vote_list = latest_attack_vote_list
        self.talk_list = talk_list
        self.whisper_list = whisper_list
        self.status_map = status_map
        self.role_map = role_map
        self.remain_talk_map = remain_talk_map
        self.remain_whisper_map = remain_whisper_map
        self.existing_role_list = existing_role_list
        self.last_dead_agent_list = last_dead_agent_list

    @classmethod
    def initialize_from_json(cls, value: dict) -> "GameInfo":
        """Initializes a GameInfo instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method takes a dictionary containing information about the game state and
        initializes a new GameInfo instance with it. The provided JSON data is expected
        to include various components such as the current day, the agent's ID, and lists
        of votes, talks, and agent statuses, among others.

        Args:
            value (dict): JSON dictionary of "gameInfo" received from the game server.
                The expected structure includes:
                - "day" (int): The current day of the game.
                - "agent" (int): The ID of the agent.
                - "voteList" (list): The list of votes cast.
                - "latestVoteList" (list): The list of the latest votes.
                - "attackVoteList" (list): The list of attack votes.
                - "latestAttackVoteList" (list): The list of the latest attack votes.
                - "talkList" (list): The list of talks made by agents.
                - "whisperList" (list): The list of whispers made by agents.
                - "statusMap" (dict): The current status of agents.
                - "roleMap" (dict): The roles assigned to agents.
                - "remainTalkMap" (dict): The remaining talk counts for agents.
                - "remainWhisperMap" (dict): The remaining whisper counts for agents.
                - "existingRoleList" (list): The list of existing roles in the game.
                - "lastDeadAgentList" (list): The list of agents that have died.

        Returns:
            GameInfo: An instance of GameInfo initialized with the provided JSON data.
        """
        return cls(
            day=value["day"],
            agent=value["agent"],
            vote_list=VoteList.initialize_from_json(value["voteList"]),
            latest_vote_list=VoteList.initialize_from_json(value["latestVoteList"]),
            attack_vote_list=VoteList.initialize_from_json(value["attackVoteList"]),
            latest_attack_vote_list=VoteList.initialize_from_json(value["latestAttackVoteList"]),
            talk_list=TalkList.initialize_from_json(value["talkList"]),
            whisper_list=TalkList.initialize_from_json(value["whisperList"]),
            status_map=StatusMap.initialize_from_json(value["statusMap"]),
            role_map=RoleMap.initialize_from_json(value["roleMap"]),
            remain_talk_map=RemainTalkMap.initialize_from_json(value["remainTalkMap"]),
            remain_whisper_map=RemainTalkMap.initialize_from_json(value["remainWhisperMap"]),
            existing_role_list=ExistingRoleList.initialize_from_json(value["existingRoleList"]),
            last_dead_agent_list=LastDeadAgentList.initialize_from_json(value["lastDeadAgentList"]),
        )
