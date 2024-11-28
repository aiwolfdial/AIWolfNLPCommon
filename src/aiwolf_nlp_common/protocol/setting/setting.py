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

    def __init__(self, value: dict | None = None) -> None:
        if value is not None:
            self.role_num_map = RoleNumMap(value=value["roleNumMap"])
            self.max_talk = value["maxTalk"]
            self.max_talk_turn = value["maxTalkTurn"]
            self.max_whisper = value["maxWhisper"]
            self.max_whisper_turn = value["maxWhisperTurn"]
            self.max_skip = value["maxSkip"]
            self.is_enable_no_attack = value["isEnableNoAttack"]
            self.is_vote_visible = value["isVoteVisible"]
            self.is_talk_on_first_day = value["isTalkOnFirstDay"]
            self.response_timeout = value["responseTimeout"] // 1000
            self.action_timeout = value["actionTimeout"] // 1000
            self.max_revote = value["maxRevote"]
            self.max_attack_revote = value["maxAttackRevote"]
            self.player_num = value["playerNum"]

    def update(self, value: dict | None) -> None:
        self.__init__(value)
