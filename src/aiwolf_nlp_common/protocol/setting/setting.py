"""Defines GameSetting class for werewolf game configuration management.

The GameSetting class encapsulates various parameters and rules for the game, as received from a
game server. It includes information such as:
- Role distribution
- Limits on talking and whispering
- Voting and attack rules
- Time limits for actions and responses
- Special game modes (e.g., no attack, visible votes)

The class provides methods for initializing these settings either directly or from a JSON object
received from the game server.

Classes:
    GameSetting: Represents the complete set of game settings.

Imports:
    .map.role_num_map.RoleNumMap: Imported to handle role distribution information.

Note:
    This module is designed to work with a specific game server protocol. Ensure that the
    server's JSON format matches the expected structure in the initialize_from_json method.s
    This description was written by Claude 3.5 Sonnet.
"""

from __future__ import annotations

from .map.role_num_map import RoleNumMap


class Setting:
    """Class for storing “gameSetting” information received from the game server."""

    __ms_to_seconds_divisor: int = 1000

    role_num_map: RoleNumMap
    max_talk: int
    max_talk_turn: int
    max_whisper: int
    max_whisper_turn: int
    max_skip: int
    is_enable_no_attack: bool
    is_vote_visible: bool
    is_talk_on_first_day: bool
    response_timeout: int
    action_timeout: int
    max_revote: int
    max_attack_revote: int
    player_num: int

    def __init__(
        self,
        role_num_map: RoleNumMap,
        max_talk: int,
        max_talk_turn: int,
        max_whisper: int,
        max_whisper_turn: int,
        max_skip: int,
        is_enable_no_attack: bool,
        is_vote_visible: bool,
        is_talk_on_first_day: bool,
        response_timeout: int,
        action_timeout: int,
        max_revote: int,
        max_attack_revote: int,
        player_num: int,
    ) -> None:
        """Initialize “GameSetting”.

        This description was written by Claude 3.5 Sonnet.

        Args:
            role_num_map (RoleNumMap): Information on “roleNumMap” received from the
                game server.
            max_talk (int): Information on “maxTalk” received from the game server.
            max_talk_turn (int): Information on “maxTalkTurn” received from the game
                server.
            max_whisper (int): Information on “maxWhisper” received from the game
                server.
            max_whisper_turn (int): Information on “maxWhisperTurn” received from the
                game server.
            max_skip (int): Information on “maxSkip” received from the game server.
            is_enable_no_attack (bool): Whether "no attack" is allowed, as received from
                the game server.
            is_vote_visible (bool): Whether the voting results are visible, as received
                from the game server.
            is_talk_on_first_day (bool): Whether talking is allowed on the first day, as
                received from the game server.
            response_timeout (int): The time limit for responses in seconds, as received
                from the game server.
            action_timeout (int): The time limit for actions in seconds, as received from
                the game server.
            max_revote (int): The maximum number of revotes allowed, as received from
                the game server.
            max_attack_revote (int): The maximum number of revotes allowed for attacks,
                as received from the game server.
            player_num (int): The number of players in the game, as received from the
                game server.
        """
        self.role_num_map = role_num_map
        self.max_talk = max_talk
        self.max_talk_turn = max_talk_turn
        self.max_whisper = max_whisper
        self.max_whisper_turn = max_whisper_turn
        self.max_skip = max_skip
        self.is_enable_no_attack = is_enable_no_attack
        self.is_vote_visible = is_vote_visible
        self.is_talk_on_first_day = is_talk_on_first_day
        self.response_timeout = response_timeout
        self.action_timeout = action_timeout
        self.max_revote = max_revote
        self.max_attack_revote = max_attack_revote
        self.player_num = player_num

    def __str__(self) -> str:
        return (
            f"{self.role_num_map}\n\n"
            f"MaxTalk: {self.max_talk}\n"
            f"MaxTalkTurn: {self.max_talk_turn}\n"
            f"MaxWhisper: {self.max_whisper}\n"
            f"MaxWhisperTurn: {self.max_whisper_turn}\n"
            f"MaxSkip: {self.max_skip}\n"
            f"isEnableNoAttack: {self.is_enable_no_attack}\n"
            f"isVoteVisible: {self.is_vote_visible}\n"
            f"isTalkOnFirstDay: {self.is_talk_on_first_day}\n"
            f"ResponseTimeOut: {self.response_timeout}\n"
            f"ActionTimeOut: {self.action_timeout}\n"
            f"MaxReVote: {self.max_revote}\n"
            f"MaxAttackReVote: {self.max_attack_revote}\n"
            f"PlayerNum: {self.player_num}\n"
        )

    @classmethod
    def convert_ms_to_seconds(cls, time: int) -> int:
        return int(time / cls.__ms_to_seconds_divisor)

    def get_action_timeout_in_seconds(self) -> int:
        """Convert and retrieve the action timeout in seconds.

        This method converts the `action_timeout` value, which is stored in milliseconds,
        to seconds and returns the result as an integer.

        Returns:
            int: The action timeout value in seconds.
        """
        return int(self.action_timeout / 1000)

    @classmethod
    def initialize_from_json(cls, value: dict) -> "Setting":
        """Initialize with information received from the game server.

        Args:
            value (dict): json dict of “gameSetting” received from the game server.
        """
        return cls(
            role_num_map=RoleNumMap.initialize_from_json(value=value["roleNumMap"]),
            max_talk=value["maxTalk"],
            max_talk_turn=value["maxTalkTurn"],
            max_whisper=value["maxWhisper"],
            max_whisper_turn=value["maxWhisperTurn"],
            max_skip=value["maxSkip"],
            is_enable_no_attack=value["isEnableNoAttack"],
            is_vote_visible=value["isVoteVisible"],
            is_talk_on_first_day=value["isTalkOnFirstDay"],
            response_timeout=cls.convert_ms_to_seconds(time=value["responseTimeout"]),
            action_timeout=cls.convert_ms_to_seconds(time=value["actionTimeout"]),
            max_revote=value["maxRevote"],
            max_attack_revote=value["maxAttackRevote"],
            player_num=value["playerNum"],
        )

    def update_from_json(self, value: dict | None) -> None:
        if value is None:
            return None

        self.role_num_map = RoleNumMap.initialize_from_json(value=value["roleNumMap"])
        self.max_talk = value["maxTalk"]
        self.max_talk_turn = value["maxTalkTurn"]
        self.max_whisper = value["maxWhisper"]
        self.max_whisper_turn = value["maxWhisperTurn"]
        self.max_skip = value["maxSkip"]
        self.is_enable_no_attack = value["isEnableNoAttack"]
        self.is_vote_visible = value["isVoteVisible"]
        self.is_talk_on_first_day = value["isTalkOnFirstDay"]
        self.response_timeout = self.convert_ms_to_seconds(time=value["responseTimeout"])
        self.action_timeout = self.convert_ms_to_seconds(time=value["actionTimeout"])
        self.max_revote = value["maxRevote"]
        self.max_attack_revote = value["maxAttackRevote"]
        self.player_num = value["playerNum"]
