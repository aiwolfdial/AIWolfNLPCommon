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
