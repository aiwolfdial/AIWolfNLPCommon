from aiwolf_nlp_common.protocol.list.existing_role_list import ExistingRoleList
from aiwolf_nlp_common.role.role import AIWolfNLPRoleInfo


def test_set_received_info(initialize_json:dict, vote_list_json:dict) -> None:
    vote_list = ExistingRoleList()
    vote_list.set_received_info(set_list=initialize_json["gameInfo"]["existingRoleList"])

    check_list = [AIWolfNLPRoleInfo.POSSESSED, AIWolfNLPRoleInfo.SEER, AIWolfNLPRoleInfo.VILLAGER, AIWolfNLPRoleInfo.WEREWOLF]

    assert vote_list == check_list