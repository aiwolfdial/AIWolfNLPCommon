"""This module defines the Day enum class."""

import enum


class Day(enum.Enum):
    """Enum class representing the day of the game."""

    GREETING_DAY = 0

    @classmethod
    def is_greeting_day(cls, day: int) -> bool:
        """Checks if the given day is the greeting day."""
        return day == cls.GREETING_DAY
