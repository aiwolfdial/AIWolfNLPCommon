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
    server's JSON format matches the expected structure in the initialize_from_json method.
    This description was written by Claude 3.5 Sonnet.
"""

from .map.role_num_map import RoleNumMap


class GameSetting:
    """Class for storing “gameSetting” information received from the game server."""

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
    is_enable_role_request: bool
    playe_num: int

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
        is_enable_role_request: bool,
        player_num: int,
    ) -> None:
        """Initialize “GameSetting”.

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
            is_enable_role_request (bool): Whether role requests are enabled, as received
                from the game server.
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
        self.is_enable_role_request = is_enable_role_request
        self.playe_num = player_num

    @classmethod
    def initialize_from_json(cls, value: dict) -> "GameSetting":
        """Initialize with information received from the game server.

        Args:
            value (dict): json dict of “gameSetting” received from the game server.
        """
        return cls(
            value["roleNumMap"],
            value["maxTalk"],
            value["maxTalkTurn"],
            value["maxWhisper"],
            value["maxWhisperTurn"],
            value["maxSkip"],
            value["isEnableNoAttack"],
            value["isVoteVisible"],
            value["isTalkOnFirstDay"],
            value["responseTimeout"],
            value["actionTimeout"],
            value["maxRevote"],
            value["maxAttackRevote"],
            value["isEnableRoleRequest"],
            value["playerNum"],
        )
