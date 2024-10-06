"""This module describes the team of roles sent from AIWolfNLP's game server."""

import enum


class AIWolfNLPRoleTeam:
    """A class that manages information about role teams."""

    __en: str
    __ja: str

    def __init__(self, en: str, ja: str) -> None:
        """Initialize information about the role team.

        Args:
            en (str): The English name of the role team.
            ja (str): The Japanese name of the role team.
        """
        self.__en = en
        self.__ja = ja

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “AIWolfNLPRoleTeam”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if the all values are the same., False otherwise.
        """
        return self.en == value.en and self.ja == value.ja

    @property
    def en(self) -> str:
        """Returns the role team assigned at init in English.

        Returns:
        str: Role in English.

        """
        return self.__en

    @property
    def ja(self) -> str:
        """Returns the role team assigned at init in Japanese.

        Returns:
        str: Role in Japanese.

        """
        return self.__ja


class AIWolfNLPRoleTeamInfo(enum.Enum):
    """This class defines the team of role sent from AIWolfNLP's game server."""

    VILLAGER_TEAM = AIWolfNLPRoleTeam(en="VILLAGER", ja="村人陣営")
    WEREWOLF_TEAM = AIWolfNLPRoleTeam(en="WEREWOLF", ja="人狼陣営")
    FOX_TEAM = AIWolfNLPRoleTeam(en="FOX", ja="妖狐陣営")
    ANY_TEAM = AIWolfNLPRoleTeam(en="ANY", ja="?陣営")
