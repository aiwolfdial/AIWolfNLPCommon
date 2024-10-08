"""This module defines the actions that an agent can perform in the AIWolfNLP game.

It uses an enumeration to represent the various actions required by the game server,
such as initialization, naming, role assignment, and specific actions like talking,
voting, divine actions, and attacks. The class provides class methods to check if
the incoming request matches one of the predefined actions, allowing for streamlined
handling of the game's requests.
"""

from __future__ import annotations

import enum


class Action(enum.Enum):
    """This class declares the agent's behavior as required by the game server in AIWolfNLP."""

    INITIALIZE = "INITIALIZE"
    NAME = "NAME"
    ROLE = "ROLE"
    DAILY_INITIALIZE = "DAILY_INITIALIZE"
    DAILY_FINISH = "DAILY_FINISH"
    TALK = "TALK"
    VOTE = "VOTE"
    DIVINE = "DIVINE"
    ATTACK = "ATTACK"
    WHISPER = "WHISPER"
    FINISH = "FINISH"

    @classmethod
    def is_initialize(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "INITIALIZE".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "INITIALIZE", False otherwise.

        """
        return request in {cls.INITIALIZE, cls.INITIALIZE.value}

    @classmethod
    def is_name(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "NAME".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "NAME", False otherwise.

        """
        return request in {cls.NAME, cls.NAME.value}

    @classmethod
    def is_role(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "ROLE".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "ROLE", False otherwise.

        """
        return request in {cls.ROLE, cls.ROLE.value}

    @classmethod
    def is_daily_initialize(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "DAILY_INITIALIZE".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "DAILY_INITIALIZE", False otherwise.

        """
        return request in {cls.DAILY_INITIALIZE, cls.DAILY_INITIALIZE.value}

    @classmethod
    def is_daily_finish(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "DAILY_FINISH".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "DAILY_FINISH", False otherwise.

        """
        return request in {cls.DAILY_FINISH, cls.DAILY_FINISH.value}

    @classmethod
    def is_talk(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "TALK".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "TALK", False otherwise.

        """
        return request in {cls.TALK, cls.TALK.value}

    @classmethod
    def is_vote(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "VOTE".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "VOTE", False otherwise.

        """
        return request in {cls.VOTE, cls.VOTE.value}

    @classmethod
    def is_divine(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "DIVINE".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "DIVINE", False otherwise.

        """
        return request in {cls.DIVINE, cls.DIVINE.value}

    @classmethod
    def is_attack(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "ATTACK".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "ATTACK", False otherwise.

        """
        return request in {cls.ATTACK, cls.ATTACK.value}

    @classmethod
    def is_whisper(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "WHISPER".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "WHISPER", False otherwise.

        """
        return request in {cls.WHISPER, cls.WHISPER.value}

    @classmethod
    def is_finish(cls, request: str | Action) -> bool:
        """Check if the value associated with the "request" key is "FINISH".

        Args:
                request (str): The value associated with the "request" key
                                                sent from the game server.

        Returns:
                bool: True if the value is "FINISH", False otherwise.

        """
        return request in {cls.FINISH, cls.FINISH.value}
