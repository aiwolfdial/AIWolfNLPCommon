from aiwolf_nlp_common.protocol.gameInfo.list.existing_role_list import ExistingRoleList
from aiwolf_nlp_common.role.role import RoleInfo


def test_set_received_info(initialize_json: dict) -> None:
    vote_list = ExistingRoleList.initialize_from_json(
        set_list=initialize_json["gameInfo"]["existingRoleList"]
    )

    check_list = [
        RoleInfo.POSSESSED.value,
        RoleInfo.SEER.value,
        RoleInfo.VILLAGER.value,
        RoleInfo.WEREWOLF.value,
    ]

    assert vote_list == check_list
