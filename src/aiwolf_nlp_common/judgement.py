"""This module defines the Judgement enum class."""

import enum


class Judgement(enum.Enum):
    """Enum class representing the judgement of the agent in the game."""

    HUMAN = "HUMAN"
    WEREWOLF = "WEREWOLF"

    @classmethod
    def is_human(cls, result: str) -> bool:
        """Checks if the given result represents 'human'."""
        return result in {cls.HUMAN, cls.HUMAN.value}

    @classmethod
    def is_werewolf(cls, result: str) -> bool:
        """Checks if the given result represents 'werewolf'."""
        return result in {cls.WEREWOLF, cls.WEREWOLF.value}
