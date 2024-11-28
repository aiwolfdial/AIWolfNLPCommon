from __future__ import annotations

from aiwolf_nlp_common.role import RoleInfo


class ExistingRoleList(list):
    @classmethod
    def initialize_from_json(cls, value: list[str] | None = None) -> ExistingRoleList:
        if value is None:
            return cls()
        return cls([RoleInfo.get_role_info(role=role) for role in value])
