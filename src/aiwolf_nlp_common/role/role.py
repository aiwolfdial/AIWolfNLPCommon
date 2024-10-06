"""This module describes the role sent by the game server in AIWolfNLP."""

from __future__ import annotations

import enum

from .role_team import AIWolfNLPRoleTeam, AIWolfNLPRoleTeamInfo

LANGUAGE = 2

EN_POS = 1
JA_POS = 2
TEAM_POS = 3


class AIWolfNLPRole:
    """Class that manages information about the role."""

    __en: str
    __ja: str
    __team: AIWolfNLPRoleTeam

    def __init__(self, en: str, ja: str, team: AIWolfNLPRoleTeam) -> None:
        """Initialize information about the role.

        Args:
            en (str): The English name of the role.
            ja (str): The Japanese name of the role.
            team (AIWolfNLPRoleTeam): The team to which the role belongs.
        """
        self.__en = en
        self.__ja = ja
        self.__team = team

    @property
    def en(self) -> str:
        """Returns the role assigned at init in English.

        Returns:
        str: Role in English.
        """
        return self.__en

    @property
    def ja(self) -> str:
        """Returns the role assigned at init in Japanese.

        Returns:
        str: Role in Japanese.
        """
        return self.__ja

    @property
    def team(self) -> AIWolfNLPRoleTeam:
        """Returns the team of role assigned at init.

        Returns:
        AIWolfNLPRoleTeam: Team of role.
        """
        return self.__team

    def get_translations(self) -> set:
        """Get the English and Japanese of the role assigned at init.

        Returns:
        set: Role in English and Japanese.
        """
        return {self.__en, self.__ja}


class AIWolfNLPRoleInfo(enum.Enum):
    """A class that declares information about positions sent by the game server in AIWolfNLP."""

    # villager team
    VILLAGER = AIWolfNLPRole(en="VILLAGER", ja="村人", team=AIWolfNLPRoleTeamInfo.VILLAGER_TEAM)
    SEER = AIWolfNLPRole(en="SEER", ja="占い師", team=AIWolfNLPRoleTeamInfo.VILLAGER_TEAM)
    MEDIUM = AIWolfNLPRole(en="MEDIUM", ja="霊媒師", team=AIWolfNLPRoleTeamInfo.VILLAGER_TEAM)
    BODYGUARD = AIWolfNLPRole(en="BODYGUARD", ja="騎士", team=AIWolfNLPRoleTeamInfo.VILLAGER_TEAM)
    FREEMASON = AIWolfNLPRole(en="FREEMASON", ja="共有者", team=AIWolfNLPRoleTeamInfo.VILLAGER_TEAM)

    # werewolf team
    WEREWOLF = AIWolfNLPRole(en="WEREWOLF", ja="人狼", team=AIWolfNLPRoleTeamInfo.WEREWOLF_TEAM)
    POSSESSED = AIWolfNLPRole(en="POSSESSED", ja="狂人", team=AIWolfNLPRoleTeamInfo.WEREWOLF_TEAM)

    # fox team
    FOX = AIWolfNLPRole(en="FOX", ja="妖狐", team=AIWolfNLPRoleTeamInfo.FOX_TEAM)

    # any team
    ANY = AIWolfNLPRole(en="ANY", ja="?", team=AIWolfNLPRoleTeamInfo.ANY_TEAM)

    @classmethod
    def is_exist_role(cls, role: str) -> bool:
        """Check to see if the role exists.

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            bool: True if the value is an existing role, False otherwise.
        """
        is_exist = False

        for role_info in cls.__members__.values():
            if role in role_info.value.get_translations():
                is_exist = True

        return is_exist

    @classmethod
    def is_villager(cls, role: str) -> bool:
        """Check if the value associated with the "role" key is either "VILLAGER" or "村人".

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            bool: True if the value is "VILLAGER" or "村人", False otherwise.
        """
        return role in cls.VILLAGER.value.get_translations()

    @classmethod
    def is_seer(cls, role: str) -> bool:
        """Check if the value associated with the "role" key is either "SEER" or "占い師".

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            bool: True if the value is "SEER" or "占い師", False otherwise.
        """
        return role in cls.SEER.value.get_translations()

    @classmethod
    def is_medium(cls, role: str) -> bool:
        """Check if the value associated with the "role" key is either "MEDIUM" or "霊媒師".

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            bool: True if the value is "MEDIUM" or "霊媒師", False otherwise.
        """
        return role in cls.MEDIUM.value.get_translations()

    @classmethod
    def is_bodyguard(cls, role: str) -> bool:
        """Check if the value associated with the "role" key is either "BODYGUARD" or "騎士".

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            bool: True if the value is "BODYGUARD" or "騎士", False otherwise.
        """
        return role in cls.BODYGUARD.value.get_translations()

    @classmethod
    def is_werewolf(cls, role: str) -> bool:
        """Check if the value associated with the "role" key is either "WEREWOLF" or "人狼".

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            bool: True if the value is "WEREWOLF" or "人狼", False otherwise.
        """
        return role in cls.WEREWOLF.value.get_translations()

    @classmethod
    def is_possessed(cls, role: str) -> bool:
        """Check if the value associated with the "role" key is either "POSSESSED" or "狂人".

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            bool: True if the value is "POSSESSED" or "狂人", False otherwise.
        """
        return role in cls.POSSESSED.value.get_translations()

    @classmethod
    def is_villager_team(cls, role: str) -> bool | ValueError:
        """Check if the value associated with the "role" key belongs to the Villager team.

        Args:
        role (str): The value associated with the "role" key sent from the game server.

        Returns:
        bool: True if the value represents a role from the Villager team, False otherwise.

        Raises:
                    ValueError: If a non-existent role is entered.
        """
        if not cls.is_exist_role(role=role):
            raise ValueError(role + "is not exist role.")

        for role_info in cls.__members__.values():
            if role in role_info.value.get_translations():
                return role_info.value.team == AIWolfNLPRoleTeamInfo.VILLAGER_TEAM
        return None

    @classmethod
    def is_werewolf_team(cls, role: str) -> bool | ValueError:
        """Check if the value associated with the "role" key belongs to the Werewolf team.

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            bool: True if the value represents a role from the Werewolf team, False otherwise.

        Raises:
            ValueError: If a non-existent role is entered.
        """
        if not cls.is_exist_role(role=role):
            raise ValueError(role + "is not exist role.")

        for role_info in cls.__members__.values():
            if role in role_info.value.get_translations():
                return role_info.value.team == AIWolfNLPRoleTeamInfo.WEREWOLF_TEAM
        return None

    @classmethod
    def get_role_info(cls, role: str) -> AIWolfNLPRoleInfo:
        """Get the AIWolfNLPRoleInfo instance for the role that matches the argument.

        Args:
            role (str): The value associated with the "role" key sent from the game server.

        Returns:
            AIWolfNLPRoleInfo: The AIWolfNLPRoleInfo instance that corresponds to the given role.

        Raises:
            ValueError: If a non-existent role is provided.
        """
        for role_info in cls.__members__.values():
            if role in role_info.value.get_translations():
                return role_info.value

        raise ValueError(role + "is not exist role.")

    @classmethod
    def get_villager_ja(cls) -> str:
        """Retrieve the Japanese name for the "VILLAGER" role.

        Returns:
            str: The Japanese name for the "VILLAGER" role.
        """
        return cls.VILLAGER.value.ja

    @classmethod
    def get_seer_ja(cls) -> str:
        """Retrieve the Japanese name for the "SEER" role.

        Returns:
            str: The Japanese name for the "SEER" role.
        """
        return cls.SEER.value.ja

    @classmethod
    def get_medium_ja(cls) -> str:
        """Retrieve the Japanese name for the "MEDIUM" role.

        Returns:
            str: The Japanese name for the "MEDIUM" role.
        """
        return cls.MEDIUM.value.ja

    @classmethod
    def get_werewolf_ja(cls) -> str:
        """Retrieve the Japanese name for the "WEREWOLF" role.

        Returns:
            str: The Japanese name for the "WEREWOLF" role.
        """
        return cls.WEREWOLF.value.ja

    @classmethod
    def get_possessed_ja(cls) -> str:
        """Retrieve the Japanese name for the "POSSESSED" role.

        Returns:
            str: The Japanese name for the "POSSESSED" role.
        """
        return cls.POSSESSED.value.ja
