"""This method is used to define a class for storing “roleNumMap” information."""

from aiwolf_nlp_common.role import AIWolfNLPRole, AIWolfNLPRoleInfo


class RoleNumInfo:
    """Class for defining elements of “roleNumMap”."""

    __role: AIWolfNLPRole
    __allocated_count: int

    def __init__(self, role: str, allocated_count: int) -> None:
        """Initialize “RoleNumInfo”.

        Args:
            role (str): String of the role.
            allocated_count (int): Number of roles assigned.
        """
        self.__role = AIWolfNLPRoleInfo.get_role_info(role=role)
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

    @property
    def role(self) -> AIWolfNLPRole:
        """Gets the role.

        Returns:
            AIWolfNLPRoleInfo: role information.
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

    @staticmethod
    def object_hook(value: dict) -> "RoleNumMap":
        """Stores information sent from the game server in class variables.

        Args:
            value (dict): Information on “roleNumMap” sent from the game server.
        """
        result = RoleNumMap()

        for role in value:
            add_elem = RoleNumInfo(role=role, allocated_count=value[role])
            result.add(add_elem)

        return result
