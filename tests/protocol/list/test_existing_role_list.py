from aiwolf_nlp_common.protocol.gameInfo.list.existing_role_list import ExistingRoleList
from aiwolf_nlp_common.role.role import AIWolfNLPRoleInfo


def test_set_received_info(initialize_json:dict) -> None:
    vote_list = ExistingRoleList.initialize_from_json(set_list=initialize_json["gameInfo"]["existingRoleList"])

    check_list = [AIWolfNLPRoleInfo.POSSESSED.value, AIWolfNLPRoleInfo.SEER.value, AIWolfNLPRoleInfo.VILLAGER.value, AIWolfNLPRoleInfo.WEREWOLF.value]

    assert vote_list == check_list