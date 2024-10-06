"""This method is used to define a class for storing “roleMap” information."""

from aiwolf_nlp_common.role import AIWolfNLPRole, AIWolfNLPRoleInfo


class AgentRole:
    """Class for defining elements of “roleMap”."""

    __agent: str
    __role: AIWolfNLPRole

    def __init__(self, agent: str, role: str) -> None:
        """Initialize “AgentRole”.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.
            role (str): String of the role.
        """
        self.__agent = agent
        self.__role = AIWolfNLPRoleInfo.get_role_info(role=role)

    def __hash__(self) -> int:
        """Comparison method for making comparisons in “AgentRole”.

        Returns:
            int: Result of hashing by agent name and role string.
        """
        return hash((self.agent, self.role.en))

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “AgentRole”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if the all values are the same., False otherwise.
        """
        if value is None or not isinstance(value, AgentRole):
            return False

        return self.agent == value.agent and self.role == value.role

    @property
    def agent(self) -> str:
        """Gets the agent's name.

        This property returns the agent's name in the format "Agent[xx]",
        where "xx" is the agent's identifier.

        Returns:
            str: Agent name, such as “Agent[xx]”.
        """
        return self.__agent

    @property
    def role(self) -> AIWolfNLPRole:
        """Gets the role string.

        Returns:
            AIWolfNLPRoleInfo: role information.
        """
        return self.__role


class RoleMap(set):
    """Set extension class for storing “roleMap” information."""

    def set_received_info(self, set_map: dict) -> None:
        """Stores information sent from the game server in class variables.

        Args:
            set_map (map): Information on “roleMap” sent from the game server.
        """
        self.clear()

        if len(set_map) == 0:
            return

        for agent in set_map:
            add_elem = AgentRole(agent=agent, role=set_map[agent])
            self.add(add_elem)
