from aiwolf_nlp_common.role import RoleInfo


class ExistingRoleList(list):
    @classmethod
    def initialize_from_json(cls, set_list: list[str]) -> "ExistingRoleList":
        return cls([RoleInfo.get_role_info(role=role) for role in set_list])
