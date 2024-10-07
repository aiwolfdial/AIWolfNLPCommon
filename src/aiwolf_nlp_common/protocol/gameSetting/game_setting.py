from .map.role_num_map import RoleNumMap


class GameSetting:
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
        playe_num: int,
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
        self.is_enable_role_request = is_enable_role_request
        self.playe_num = playe_num
