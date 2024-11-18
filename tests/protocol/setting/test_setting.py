from aiwolf_nlp_common.protocol.setting import Setting
from aiwolf_nlp_common.role import RoleInfo


def test_info(initialize_json):
    setting_key = "setting"
    setting = Setting.initialize_from_json(value=initialize_json[setting_key])

    assert setting.role_num_map.get_role_num(role=RoleInfo.get_villager_ja()) == 2
    assert (
        setting.role_num_map.get_role_num(role=RoleInfo.VILLAGER)
        == initialize_json[setting_key]["roleNumMap"]["VILLAGER"]
    )
    assert (
        setting.role_num_map.get_role_num(role=RoleInfo.VILLAGER.value)
        == initialize_json[setting_key]["roleNumMap"]["VILLAGER"]
    )
    assert setting.max_talk == initialize_json[setting_key]["maxTalk"]
    assert setting.max_talk_turn == initialize_json[setting_key]["maxTalkTurn"]
    assert setting.max_whisper == initialize_json[setting_key]["maxWhisper"]
    assert setting.max_whisper_turn == initialize_json[setting_key]["maxWhisperTurn"]
    assert setting.max_skip == initialize_json[setting_key]["maxSkip"]
    assert setting.is_enable_no_attack == bool(initialize_json[setting_key]["isEnableNoAttack"])
    assert setting.is_vote_visible == bool(initialize_json[setting_key]["isVoteVisible"])
    assert setting.is_talk_on_first_day == bool(initialize_json[setting_key]["isTalkOnFirstDay"])
    assert setting.response_timeout == Setting.convert_ms_to_seconds(
        time=initialize_json[setting_key]["responseTimeout"]
    )
    assert setting.action_timeout == Setting.convert_ms_to_seconds(
        time=initialize_json[setting_key]["actionTimeout"]
    )
    assert setting.max_revote == initialize_json[setting_key]["maxRevote"]
    assert setting.max_attack_revote == initialize_json[setting_key]["maxAttackRevote"]
