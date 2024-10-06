"""This method is used to define a class for storing “statusMap” information."""

from __future__ import annotations

import enum
from typing import Literal


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
    __status: Literal[Status.ALIVE, Status.DEAD]

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
            bool: True if the all values are the same., False otherwise.
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
    def status(self) -> Status.ALIVE | Status.DEAD:
        """Gets the status.

        Returns:
            Status.ALIVE | Status.DEAD: status.
        """
        return self.__status


class StatusMap(set):
    """Set extension class for storing “statusMap” information."""

    def reverse_status(self, agent: str) -> None | ValueError:
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

    def set_received_info(self, set_map: dict) -> None:
        """Stores information sent from the game server in class variables.

        Args:
            set_map (map): Information on “statusMap” sent from the game server.
        """
        self.clear()

        if len(set_map) == 0:
            return

        for agent in set_map:
            add_elem = AgentStatus(agent=agent, status=set_map[agent])
            self.add(add_elem)
