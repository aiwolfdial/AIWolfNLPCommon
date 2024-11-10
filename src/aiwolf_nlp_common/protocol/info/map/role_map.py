"""This method is used to define a class for storing “roleMap” information."""

from __future__ import annotations

from aiwolf_nlp_common.role import Role, RoleInfo


class AgentRole:
    """Class for defining elements of “roleMap”."""

    __agent: str
    __role: Role

    def __init__(self, agent: str, role: str) -> None:
        """Initialize “AgentRole”.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.
            role (str): String of the role.
        """
        self.__agent = agent
        self.__role = RoleInfo.get_role_info(role=role)

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

    def __lt__(self, value: object) -> bool:
        """Comparison method for making comparisons in “AgentRole”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if all values are the same, False otherwise.
        """
        if value is None or not isinstance(value, self.__class__):
            return NotImplemented

        return self.__agent < value.__agent

    def __str__(self) -> str:
        return f"{self.__agent} is {self.__role.en}"

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
    def role(self) -> Role:
        """Gets the role.

        Returns:
            RoleInfo: role information.
        """
        return self.__role


class RoleMap(set):
    """Set extension class for storing “roleMap” information."""

    def __str__(self) -> str:
        output: str = f"[{self.__class__.__name__}]"

        if self.is_empty():
            return output + "\nNo Result Available"

        output_list = list(self)
        elem: AgentRole
        for elem in sorted(output_list):
            output += "\n" + elem.__str__()

        return output

    @classmethod
    def initialize_from_json(cls, set_map: dict) -> RoleMap:
        """Initializes a RoleMap instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method creates a new instance of the RoleMap class and populates it with
        information about the roles assigned to each agent. The provided dictionary maps
        agent identifiers to their respective roles.

        Args:
            set_map (dict): Information on “roleMap” sent from the game server.
                Each key in the dictionary is an agent identifier, and the corresponding
                value is the role assigned to that agent.

        Returns:
            RoleMap: A new RoleMap instance populated with AgentRole objects created
            from the input data.
        """
        instance = cls()

        for agent in set_map:
            add_elem = AgentRole(agent=agent, role=set_map[agent])
            instance.add(add_elem)

        return instance

    def get_role(self, agent: str) -> Role:
        """Retrieve the role of a specified agent.

        This docstring was created by a generative AI.
        This method searches for the role associated with the given agent name.
        If the agent is found, it returns the corresponding role; otherwise, it raises a ValueError.

        Args:
            agent (str): The name of the agent, formatted as “Agent[xx]”.

        Returns:
            Role: The role of the specified agent.

        Raises:
            ValueError: If the specified agent name does not exist in the current context.
        """
        for agent_role in self:
            if agent_role.agent == agent:
                return agent_role.role

        raise ValueError(agent + " is a name that does not exist.")

    def is_empty(self) -> bool:
        """Check if the object is empty.

        This method returns True if the object has no elements (i.e., its length is 0),
        and False otherwise.

        Returns:
            bool: True if the object is empty, False otherwise.
        """
        return len(self) == 0
