"""This module describes the role sent by the game server in AIWolfNLP."""

from __future__ import annotations

import enum

from .role_team import RoleTeam, RoleTeamInfo

LANGUAGE = 2

EN_POS = 1
JA_POS = 2
TEAM_POS = 3


class Role:
    """Class that manages information about the role."""

    __en: str
    __ja: str
    __team: RoleTeam

    def __init__(self, en: str, ja: str, team: RoleTeam) -> None:
        """Initialize information about the role.

        Args:
            en (str): The English name of the role.
            ja (str): The Japanese name of the role.
            team (RoleTeam): The team to which the role belongs.
        """
        self.__en = en
        self.__ja = ja
        self.__team = team

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “Role”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if the all values are the same., False otherwise.
        """
        if value is None or not isinstance(value, Role):
            return False
        return self.en == value.en and self.ja == value.ja and self.team == value.team

    def __hash__(self) -> int:
        """Return the hash value of the object.

        This method computes a hash value for the instance by combining
        the hash values of the instance's attributes: __en, __ja, and
        __team. It is useful for allowing instances of this class to be
        used as keys in dictionaries or stored in sets.

        Returns:
            int: The hash value of the object.
        """
        return hash((self.__en, self.__ja, self.__team))

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
    def team(self) -> RoleTeam:
        """Returns the team of role assigned at init.

        Returns:
        RoleTeam: Team of role.
        """
        return self.__team

    def get_translations(self) -> set:
        """Get the English and Japanese of the role assigned at init.

        Returns:
        set: Role in English and Japanese.
        """
        return {self.__en, self.__ja}


class RoleInfo(enum.Enum):
    """A class that declares information about positions sent by the game server in AIWolfNLP."""

    # villager team
    VILLAGER = Role(en="VILLAGER", ja="村人", team=RoleTeamInfo.VILLAGER_TEAM.value)
    SEER = Role(en="SEER", ja="占い師", team=RoleTeamInfo.VILLAGER_TEAM.value)
    MEDIUM = Role(en="MEDIUM", ja="霊媒師", team=RoleTeamInfo.VILLAGER_TEAM.value)
    BODYGUARD = Role(en="BODYGUARD", ja="騎士", team=RoleTeamInfo.VILLAGER_TEAM.value)
    FREEMASON = Role(en="FREEMASON", ja="共有者", team=RoleTeamInfo.VILLAGER_TEAM.value)

    # werewolf team
    WEREWOLF = Role(en="WEREWOLF", ja="人狼", team=RoleTeamInfo.WEREWOLF_TEAM.value)
    POSSESSED = Role(en="POSSESSED", ja="狂人", team=RoleTeamInfo.WEREWOLF_TEAM.value)

    # fox team
    FOX = Role(en="FOX", ja="妖狐", team=RoleTeamInfo.FOX_TEAM.value)

    # any team
    ANY = Role(en="ANY", ja="?", team=RoleTeamInfo.ANY_TEAM.value)

    @classmethod
    def is_exist_role(cls, role: str | Role) -> bool:
        """Determine if a specified role exists in the enumeration.

        This docstring was created by a generative AI.
        This method checks whether the given role, either as a string or as a Role
        instance, matches any of the roles defined in the class. It also considers
        translations of the role values.

        Args:
            role (str | Role): The role to check, which can be either a string
                or an instance of the Role enumeration.

        Returns:
            bool: True if the specified role exists, False otherwise.
        """
        is_exist = False

        for role_info in cls.__members__.values():
            if role in {role_info, role_info.value} or role in role_info.value.get_translations():
                is_exist = True

        return is_exist

    @classmethod
    def is_villager(cls, role: str | Role) -> bool:
        """Determine if the specified role is a villager.

        This docstring was created by a generative AI.
        This method checks whether the given role, either as a string or as a Role
        instance, matches the definitions of "VILLAGER" or its translations, such as "村人".

        Args:
            role (str | Role): The role to check, which can be either a string
                or an instance of the Role enumeration.

        Returns:
            bool: True if the specified role is "VILLAGER" or "村人", False otherwise.
        """
        return (
            role in {cls.VILLAGER, cls.VILLAGER.value}
            or role in cls.VILLAGER.value.get_translations()
        )

    @classmethod
    def is_seer(cls, role: str | Role) -> bool:
        """Determine if the specified role is a seer.

        This docstring was created by a generative AI.
        This method checks whether the given role, either as a string or as a Role
        instance, matches the definitions of "SEER" or its translations, such as "占い師".

        Args:
            role (str | Role): The role to check, which can be either a string
                or an instance of the Role enumeration.

        Returns:
            bool: True if the specified role is "SEER" or "占い師", False otherwise.
        """
        return role in {cls.SEER, cls.SEER.value} or role in cls.SEER.value.get_translations()

    @classmethod
    def is_medium(cls, role: str | Role) -> bool:
        """Determine if the specified role is a medium.

        This docstring was created by a generative AI.
        This method checks whether the given role, either as a string or as a Role
        instance, matches the definitions of "MEDIUM" or its translations, such as "霊媒師".

        Args:
            role (str | Role): The role to check, which can be either a string
                or an instance of the Role enumeration.

        Returns:
            bool: True if the specified role is "MEDIUM" or "霊媒師", False otherwise.
        """
        return role in {cls.MEDIUM, cls.MEDIUM.value} or role in cls.MEDIUM.value.get_translations()

    @classmethod
    def is_bodyguard(cls, role: str | Role) -> bool:
        """Determine if the specified role is a bodyguard.

        This docstring was created by a generative AI.
        This method checks whether the given role, either as a string or as a Role
        instance, matches the definitions of "BODYGUARD" or its translations, such as "騎士".

        Args:
            role (str | Role): The role to check, which can be either a string
                or an instance of the Role enumeration.

        Returns:
            bool: True if the specified role is "BODYGUARD" or "騎士", False otherwise.
        """
        return (
            role in {cls.BODYGUARD, cls.BODYGUARD.value}
            or role in cls.BODYGUARD.value.get_translations()
        )

    @classmethod
    def is_werewolf(cls, role: str | Role) -> bool:
        """Determine if the specified role is a werewolf.

        This docstring was created by a generative AI.
        This method checks whether the given role, either as a string or as a Role
        instance, matches the definitions of "WEREWOLF" or its translations, such as "人狼".

        Args:
            role (str | Role): The role to check, which can be either a string
                or an instance of the Role enumeration.

        Returns:
            bool: True if the specified role is "WEREWOLF" or "人狼", False otherwise.
        """
        return (
            role in {cls.WEREWOLF, cls.WEREWOLF.value}
            or role in cls.WEREWOLF.value.get_translations()
        )

    @classmethod
    def is_possessed(cls, role: str | Role) -> bool:
        """Determine if the specified role is a possessed player.

        This docstring was created by a generative AI.
        This method checks whether the given role, either as a string or as a Role
        instance, matches the definitions of "POSSESSED" or its translations, such as "狂人".

        Args:
            role (str | Role): The role to check, which can be either a string
                or an instance of the Role enumeration.

        Returns:
            bool: True if the specified role is "POSSESSED" or "狂人", False otherwise.
        """
        return (
            role in {cls.POSSESSED, cls.POSSESSED.value}
            or role in cls.POSSESSED.value.get_translations()
        )

    @classmethod
    def is_villager_team(cls, role: str) -> bool:
        """Check if the specified role belongs to the Villager team.

        This docstring was created by a generative AI.
        This method determines whether the provided role, as received from the game server,
        is associated with the Villager team. If the role does not exist in the current context,
        it raises a ValueError.

        Args:
            role (str): The role to check, formatted as received from the game server.

        Returns:
            bool: True if the specified role belongs to the Villager team, False otherwise.

        Raises:
            ValueError: If the provided role does not exist in the current context.
        """
        if not cls.is_exist_role(role=role):
            raise ValueError(role + "is not exist role.")

        for role_info in cls.__members__.values():
            if role in {role_info, role_info.value} or role in role_info.value.get_translations():
                return role_info.value.team == RoleTeamInfo.VILLAGER_TEAM.value

        return False

    @classmethod
    def is_werewolf_team(cls, role: str) -> bool:
        """Check if the specified role belongs to the Werewolf team.

        This docstring was created by a generative AI.
        This method determines whether the provided role, as received from the game server,
        is associated with the Werewolf team. If the role does not exist in the current context,
        it raises a ValueError.

        Args:
            role (str): The role to check, formatted as received from the game server.

        Returns:
            bool: True if the specified role belongs to the Werewolf team, False otherwise.

        Raises:
            ValueError: If the provided role does not exist in the current context.
        """
        if not cls.is_exist_role(role=role):
            raise ValueError(role + "is not exist role.")

        for role_info in cls.__members__.values():
            if role in {role_info, role_info.value} or role in role_info.value.get_translations():
                return role_info.value.team == RoleTeamInfo.WEREWOLF_TEAM.value

        return False

    @classmethod
    def get_role_info(cls, role: str) -> Role:
        """Retrieve the RoleInfo instance that corresponds to the specified role.

        This docstring was created by a generative AI.
        This method searches for the RoleInfo associated with the provided role name
        received from the game server. If the role does not exist, it raises a ValueError.

        Args:
            role (str): The role name to retrieve, as sent from the game server.

        Returns:
            RoleInfo: The RoleInfo instance associated with the specified role.

        Raises:
            ValueError: If the provided role does not exist in the current context.
        """
        for role_info in cls.__members__.values():
            if role == role_info or role in role_info.value.get_translations():
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
