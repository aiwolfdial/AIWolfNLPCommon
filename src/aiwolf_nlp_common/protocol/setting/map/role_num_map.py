"""This method is used to define a class for storing “roleNumMap” information."""

from __future__ import annotations

from aiwolf_nlp_common.role import Role, RoleInfo


class RoleNumInfo:
    """Class for defining elements of “roleNumMap”."""

    __role: Role
    __allocated_count: int

    def __init__(self, role: str, allocated_count: int) -> None:
        """Initialize “RoleNumInfo”.

        Args:
            role (str): String of the role.
            allocated_count (int): Number of roles assigned.
        """
        self.__role = RoleInfo.get_role_info(role=role)
        self.__allocated_count = allocated_count

    def __hash__(self) -> int:
        """Comparison method for making comparisons in “RoleNumInfo”.

        Returns:
            int: Result of hashing by role name and allocated_count.
        """
        return hash((self.__role.en, self.__allocated_count))

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “RoleNumInfok”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if the all values are the same., False otherwise.
        """
        if value is None or not isinstance(value, RoleNumInfo):
            return False

        return self.__role == value.role and self.__allocated_count == value.allocated_count

    def __lt__(self, value: object) -> bool:
        """Comparison method for making comparisons in “RoleNumInfo”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if all values are the same, False otherwise.
        """
        if value is None or not isinstance(value, self.__class__):
            return NotImplemented

        return self.__role.en < value.__role.en

    def __str__(self) -> str:
        return f"{self.__role.en} : {self.__allocated_count}"

    @property
    def role(self) -> Role:
        """Gets the role.

        Returns:
            RoleInfo: role information.
        """
        return self.__role

    @property
    def allocated_count(self) -> int:
        """Gets the allocated_count.

        Returns:
            int: Number of roles assigned.
        """
        return self.__allocated_count


class RoleNumMap(set):
    """Set extension class for storing “roleNumMap” information."""

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
    def initialize_from_json(cls, value: dict) -> RoleNumMap:
        """Stores information sent from the game server in class variables.

        Args:
            value (dict): Information on “roleNumMap” sent from the game server.
        """
        result = RoleNumMap()

        for role in value:
            add_elem = RoleNumInfo(role=role, allocated_count=value[role])
            result.add(add_elem)

        return result

    def get_role_num(self, role: str | Role) -> int:
        """Retrieve the number of allocated instances for a specified role.

        This docstring was created by a generative AI.
        This method retrieves the count of allocated instances for a
        specified role, identified either by its name as a string or
        by an instance of the Role enum. If the specified role is not
        found, it raises a ValueError.

        Args:
            role (str | Role): The name of the role as a string or
            an instance of the Role enum.

        Returns:
            int: The number of allocated instances for the specified role.

        Raises:
            ValueError: If the specified role does not exist in the
            current context or if it has not been added yet.

        Examples:
            >>> instance = RoleNumMap()
            >>> instance.get_role_num('WEREWOLF')
            1
            >>> instance.get_role_num(Role.VILLAGER)
            2
        """
        if not RoleInfo.is_exist_role(role=role):
            raise ValueError(role + " is a nonexistent role.")

        if not isinstance(role, Role):
            role = RoleInfo.get_role_info(role=role)

        for role_num_info in self:
            if role_num_info.role == role:
                return role_num_info.allocated_count

        raise ValueError(role + " has not been added.")

    def is_empty(self) -> bool:
        """Check if the object is empty.

        This method returns True if the object has no elements (i.e., its length is 0),
        and False otherwise.

        Returns:
            bool: True if the object is empty, False otherwise.
        """
        return len(self) == 0
