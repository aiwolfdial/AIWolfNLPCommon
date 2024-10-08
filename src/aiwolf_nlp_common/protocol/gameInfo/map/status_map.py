"""This method is used to define a class for storing “statusMap” information."""

from __future__ import annotations

import enum


class Status(enum.Enum):
    """An enumeration representing the possible status of a player in the game.

    This enum defines two possible states for a player: "ALIVE" and "DEAD".
    It includes a class method to check if a given status string represents the "ALIVE" status.

    Attributes:
        ALIVE (str): Represents the "ALIVE" state.
        DEAD (str): Represents the "DEAD" state.

    Methods:
        is_alive(cls, status: str) -> bool:
            Checks if the given status string is equal to the "ALIVE" status.
    """

    ALIVE = "ALIVE"
    DEAD = "DEAD"

    @classmethod
    def is_alive(cls, status: str) -> bool:
        """Check if the given status is equal to the class's "ALIVE" status.

        Args:
            status (str): The status string to check.

        Returns:
            bool: True if the status string is equal to the class's ALIVE status, False otherwise.
        """
        return status == cls.ALIVE.value


class AgentStatus:
    """Class for defining elements of “statusMap”."""

    __agent: str
    __status: Status

    def __init__(self, agent: str, status: str) -> None:
        """Initialize “AgentStatus”.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.
            status (str): String of the status.
        """
        self.__agent = agent
        self.__status = Status.ALIVE if Status.is_alive(status=status) else Status.DEAD

    def __hash__(self) -> int:
        """Comparison method for making comparisons in “AgentStatus”.

        Returns:
            int: Result of hashing by agent name and status.
        """
        return hash((self.agent, self.status.value))

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “AgentStatus”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if all values are the same, False otherwise.
        """
        if value is None or not isinstance(value, AgentStatus):
            return False
        return self.agent == value.agent and self.status.value == value.status.value

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
    def status(self) -> Status:
        """Gets the status.

        Returns:
            Status.ALIVE | Status.DEAD: status.
        """
        return self.__status


class StatusMap(set):
    """Set extension class for storing “statusMap” information."""

    @classmethod
    def initialize_from_json(cls, set_map: dict) -> StatusMap:
        """Initializes a StatusMap instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method creates a new instance of the StatusMap class and populates it with
        information about the statuses assigned to each agent. The provided dictionary maps
        agent identifiers to their respective statuses.

        Args:
            set_map (dict): Information on “statusMap” sent from the game server.
                Each key in the dictionary is an agent identifier, and the corresponding
                value is the status assigned to that agent.

        Returns:
            StatusMap: A new StatusMap instance populated with AgentStatus objects created
            from the input data.
        """
        instance = cls()

        for agent in set_map:
            add_elem = AgentStatus(agent=agent, status=set_map[agent])
            instance.add(add_elem)

        return instance

    def reverse_status(self, agent: str) -> None:
        """Reverses the status of the agent.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.

        Raises:
            ValueError: If the agent's status is not registered.
        """
        prev_alive = AgentStatus(agent=agent, status=Status.ALIVE.value)
        prev_dead = AgentStatus(agent=agent, status=Status.DEAD.value)

        if prev_alive not in self and prev_dead not in self:
            raise ValueError(agent + " does not exist in this set.")

        next_status = None

        if prev_alive in self:
            next_status = prev_dead
            self.remove(prev_alive)
            self.add(next_status)
        else:
            next_status = prev_alive
            self.remove(prev_dead)
            self.add(next_status)

    def set_alive(self, agent: str) -> None:
        """Add the agent with “ALIVE” status.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.
        """
        self.add(AgentStatus(agent=agent, status=Status.ALIVE.value))

    def set_dead(self, agent: str) -> None:
        """Add the agent with “DEAD” status.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.
        """
        self.add(AgentStatus(agent=agent, status=Status.DEAD.value))
