import enum


class RoleTeam:
    __en: str
    __ja: str

    def __init__(self, en: str, ja: str) -> None:
        self.__en = en
        self.__ja = ja

    def __eq__(self, value: object) -> bool:
        if value is None or not isinstance(value, RoleTeam):
            return False
        return self.en == value.en and self.ja == value.ja

    def __hash__(self) -> int:
        return hash((self.__en, self.__ja))

    @property
    def en(self) -> str:
        return self.__en

    @property
    def ja(self) -> str:
        return self.__ja


class RoleTeamInfo(enum.Enum):
    VILLAGER_TEAM = RoleTeam(en="VILLAGER", ja="村人陣営")
    WEREWOLF_TEAM = RoleTeam(en="WEREWOLF", ja="人狼陣営")
    FOX_TEAM = RoleTeam(en="FOX", ja="妖狐陣営")
    ANY_TEAM = RoleTeam(en="ANY", ja="?陣営")
