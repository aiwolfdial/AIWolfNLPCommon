from __future__ import annotations

import enum

from .role_team import RoleTeam, RoleTeamInfo

LANGUAGE = 2

EN_POS = 1
JA_POS = 2
TEAM_POS = 3


class Role:
    __en: str
    __ja: str
    __team: RoleTeam

    def __init__(self, en: str, ja: str, team: RoleTeam) -> None:
        self.__en = en
        self.__ja = ja
        self.__team = team

    def __eq__(self, value: object) -> bool:
        if value is None or not isinstance(value, Role):
            return False
        return self.en == value.en and self.ja == value.ja and self.team == value.team

    def __hash__(self) -> int:
        return hash((self.__en, self.__ja, self.__team))

    @property
    def en(self) -> str:
        return self.__en

    @property
    def ja(self) -> str:
        return self.__ja

    @property
    def team(self) -> RoleTeam:
        return self.__team

    def get_translations(self) -> set:
        return {self.__en, self.__ja}


class RoleInfo(enum.Enum):
    VILLAGER = Role(en="VILLAGER", ja="村人", team=RoleTeamInfo.VILLAGER_TEAM.value)
    SEER = Role(en="SEER", ja="占い師", team=RoleTeamInfo.VILLAGER_TEAM.value)
    MEDIUM = Role(en="MEDIUM", ja="霊媒師", team=RoleTeamInfo.VILLAGER_TEAM.value)
    BODYGUARD = Role(en="BODYGUARD", ja="騎士", team=RoleTeamInfo.VILLAGER_TEAM.value)
    FREEMASON = Role(en="FREEMASON", ja="共有者", team=RoleTeamInfo.VILLAGER_TEAM.value)

    WEREWOLF = Role(en="WEREWOLF", ja="人狼", team=RoleTeamInfo.WEREWOLF_TEAM.value)
    POSSESSED = Role(en="POSSESSED", ja="狂人", team=RoleTeamInfo.WEREWOLF_TEAM.value)

    FOX = Role(en="FOX", ja="妖狐", team=RoleTeamInfo.FOX_TEAM.value)

    ANY = Role(en="ANY", ja="?", team=RoleTeamInfo.ANY_TEAM.value)

    @classmethod
    def is_exist_role(cls, role: str | Role) -> bool:
        is_exist = False
        for role_info in cls.__members__.values():
            if (
                role in {role_info, role_info.value}
                or role in role_info.value.get_translations()
            ):
                is_exist = True
        return is_exist

    @classmethod
    def is_villager(cls, role: str | Role) -> bool:
        return (
            role in {cls.VILLAGER, cls.VILLAGER.value}
            or role in cls.VILLAGER.value.get_translations()
        )

    @classmethod
    def is_seer(cls, role: str | Role) -> bool:
        return (
            role in {cls.SEER, cls.SEER.value}
            or role in cls.SEER.value.get_translations()
        )

    @classmethod
    def is_medium(cls, role: str | Role) -> bool:
        return (
            role in {cls.MEDIUM, cls.MEDIUM.value}
            or role in cls.MEDIUM.value.get_translations()
        )

    @classmethod
    def is_bodyguard(cls, role: str | Role) -> bool:
        return (
            role in {cls.BODYGUARD, cls.BODYGUARD.value}
            or role in cls.BODYGUARD.value.get_translations()
        )

    @classmethod
    def is_werewolf(cls, role: str | Role) -> bool:
        return (
            role in {cls.WEREWOLF, cls.WEREWOLF.value}
            or role in cls.WEREWOLF.value.get_translations()
        )

    @classmethod
    def is_possessed(cls, role: str | Role) -> bool:
        return (
            role in {cls.POSSESSED, cls.POSSESSED.value}
            or role in cls.POSSESSED.value.get_translations()
        )

    @classmethod
    def is_villager_team(cls, role: str) -> bool:
        if not cls.is_exist_role(role=role):
            raise ValueError(role + "is not exist role.")
        for role_info in cls.__members__.values():
            if (
                role in {role_info, role_info.value}
                or role in role_info.value.get_translations()
            ):
                return role_info.value.team == RoleTeamInfo.VILLAGER_TEAM.value
        return False

    @classmethod
    def is_werewolf_team(cls, role: str) -> bool:
        if not cls.is_exist_role(role=role):
            raise ValueError(role + "is not exist role.")
        for role_info in cls.__members__.values():
            if (
                role in {role_info, role_info.value}
                or role in role_info.value.get_translations()
            ):
                return role_info.value.team == RoleTeamInfo.WEREWOLF_TEAM.value
        return False

    @classmethod
    def get_role_info(cls, role: str) -> Role:
        for role_info in cls.__members__.values():
            if role == role_info or role in role_info.value.get_translations():
                return role_info.value
        raise ValueError(role + "is not exist role.")
