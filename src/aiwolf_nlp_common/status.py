"""An enumeration representing the possible status of a player in the game.

This docstring was created by a generative AI.
This enum defines two possible states for a player: "ALIVE" and "DEAD".
It includes a method to check if a given status string is "ALIVE".

Attributes:
    ALIVE (str): Represents the "ALIVE" state.
    DEAD (str): Represents the "DEAD" state.

Methods:
    Status.is_alive: Checks if a status string is "ALIVE".
"""

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
    def is_alive(cls, status: str | Status) -> bool:
        """Determine if the provided status represents the "ALIVE" state.

        This docstring was created by a generative AI.
        This class method checks whether the given status string matches the
        enumeration value for "ALIVE". It supports both the enum member and
        its value string.

        Args:
            status (str): The status string to check.

        Returns:
            bool: True if the status string indicates that the agent is alive,
                  False otherwise.
        """
        return status in {cls.ALIVE, cls.ALIVE.value}

    @classmethod
    def is_dead(cls, status: str | Status) -> bool:
        """Determine if the provided status represents the "DEAD" state.

        This docstring was created by a generative AI.
        This class method checks whether the given status string matches the
        enumeration value for "DEAD". It supports both the enum member and
        its value string.

        Args:
            status (str): The status string to check.

        Returns:
            bool: True if the status string indicates that the agent is dead,
                  False otherwise.
        """
        return status in {cls.DEAD, cls.DEAD.value}
