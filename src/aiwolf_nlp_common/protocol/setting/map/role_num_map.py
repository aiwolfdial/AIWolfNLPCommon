from __future__ import annotations

from aiwolf_nlp_common.role import Role, RoleInfo


class RoleNumInfo:
    __role: Role
    __allocated_count: int

    def __init__(self, role: str, allocated_count: int) -> None:
        self.__role = RoleInfo.get_role_info(role=role)
        self.__allocated_count = allocated_count

    def __hash__(self) -> int:
        return hash((self.__role.en, self.__allocated_count))

    def __eq__(self, value: object) -> bool:
        if value is None or not isinstance(value, RoleNumInfo):
            return False
        return (
            self.__role == value.role
            and self.__allocated_count == value.allocated_count
        )

    def __lt__(self, value: object) -> bool:
        if value is None or not isinstance(value, self.__class__):
            return NotImplemented
        return self.__role.en < value.__role.en

    def __str__(self) -> str:
        return f"{self.__role.en} : {self.__allocated_count}"

    @property
    def role(self) -> Role:
        return self.__role

    @property
    def allocated_count(self) -> int:
        return self.__allocated_count


class RoleNumMap(set):
    def __str__(self) -> str:
        output: str = f"[{self.__class__.__name__}]"
        if self.is_empty():
            return output + "\nNo Result Available"
        output_list = list(self)
        elem: RoleNumInfo
        for elem in sorted(output_list):
            output += "\n" + elem.__str__()
        return output

    @classmethod
    def initialize_from_json(cls, value: dict | None = None) -> RoleNumMap:
        instance = cls()
        if value is None:
            return instance
        for role, count in value.items():
            instance.add(RoleNumInfo(role=role, allocated_count=count))
        return instance

    def __init__(self, value: dict | None = None) -> None:
        self.initialize_from_json(value)

    def get_role_num(self, role: str | Role) -> int:
        if not RoleInfo.is_exist_role(role=role):
            raise ValueError(role, "is a name that does not exist.")
        if not isinstance(role, Role):
            role = RoleInfo.get_role_info(role=role)
        for role_num_info in self:
            if role_num_info.role == role:
                return role_num_info.allocated_count
        raise ValueError(role, "is a name that does not exist.")

    def is_empty(self) -> bool:
        return len(self) == 0
