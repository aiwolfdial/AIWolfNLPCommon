"""This module defines the Status enum class."""

from __future__ import annotations

import enum


class Status(enum.Enum):
    """Enum class representing the status of the agent in the game."""

    ALIVE = "ALIVE"
    DEAD = "DEAD"

    @classmethod
    def is_alive(cls, status: str | Status) -> bool:
        """Checks if the given status represents 'alive'."""
        return status in {cls.ALIVE, cls.ALIVE.value}

    @classmethod
    def is_dead(cls, status: str | Status) -> bool:
        """Checks if the given status represents 'dead'."""
        return status in {cls.DEAD, cls.DEAD.value}
