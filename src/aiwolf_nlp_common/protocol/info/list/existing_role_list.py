from __future__ import annotations

from aiwolf_nlp_common.role import RoleInfo


class ExistingRoleList(list):
    def __init__(self, value: list[str] | None = None) -> None:
        super().__init__()
        if value is not None:
            self.extend(RoleInfo.get_role_info(role=role) for role in value)
