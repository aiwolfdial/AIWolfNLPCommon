from __future__ import annotations

from .map.role_num_map import RoleNumMap


class Setting:
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

    def __init__(  # noqa: PLR0913
        self,
        role_num_map: RoleNumMap,
        max_talk: int,
        max_talk_turn: int,
        max_whisper: int,
        max_whisper_turn: int,
        max_skip: int,
        is_enable_no_attack: bool,  # noqa: FBT001
        is_vote_visible: bool,  # noqa: FBT001
        is_talk_on_first_day: bool,  # noqa: FBT001
        response_timeout: int,
        action_timeout: int,
        max_revote: int,
        max_attack_revote: int,
        player_num: int,
    ) -> None:
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
    def initialize_from_json(cls, value: dict) -> Setting:
        return cls(
            role_num_map=RoleNumMap(value=value["roleNumMap"]),
            max_talk=value["maxTalk"],
            max_talk_turn=value["maxTalkTurn"],
            max_whisper=value["maxWhisper"],
            max_whisper_turn=value["maxWhisperTurn"],
            max_skip=value["maxSkip"],
            is_enable_no_attack=value["isEnableNoAttack"],
            is_vote_visible=value["isVoteVisible"],
            is_talk_on_first_day=value["isTalkOnFirstDay"],
            response_timeout=value["responseTimeout"] / 1000,
            action_timeout=value["actionTimeout"] / 1000,
            max_revote=value["maxRevote"],
            max_attack_revote=value["maxAttackRevote"],
            player_num=value["playerNum"],
        )

    def update_from_json(self, value: dict | None) -> None:
        if value is None:
            return
        self.role_num_map = RoleNumMap(value=value["roleNumMap"])
        self.max_talk = value["maxTalk"]
        self.max_talk_turn = value["maxTalkTurn"]
        self.max_whisper = value["maxWhisper"]
        self.max_whisper_turn = value["maxWhisperTurn"]
        self.max_skip = value["maxSkip"]
        self.is_enable_no_attack = value["isEnableNoAttack"]
        self.is_vote_visible = value["isVoteVisible"]
        self.is_talk_on_first_day = value["isTalkOnFirstDay"]
        self.response_timeout = int(value["responseTimeout"]) // 1000
        self.action_timeout = int(value["actionTimeout"]) // 1000
        self.max_revote = value["maxRevote"]
        self.max_attack_revote = value["maxAttackRevote"]
        self.player_num = value["playerNum"]
