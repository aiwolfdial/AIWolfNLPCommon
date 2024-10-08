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

    @classmethod
    def is_dead(cls, status: str) -> bool:
        """Check if the given status is equal to the class's "DEAD" status.

            This docstring was created by a generative AI.
            This class method compares the provided status string with the enum's
            DEAD value to determine if the agent is dead.

        Args:
            status (str): The status string to check.

        Returns:
            bool: True if the status string is equal to the class's DEAD status,
            False otherwise.
        """
        return status == cls.DEAD.value
