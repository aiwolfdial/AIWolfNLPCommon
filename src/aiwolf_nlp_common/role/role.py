import enum
from typing import Union
from .role_team import (
    AIWolfNLPRoleTeamInfo,
    AIWolfNLPRoleTeam
)

LANGUAGE = 2

EN_POS = 1
JA_POS = 2
TEAM_POS = 3

class AIWolfNLPRole():
	__en:str
	__ja:str
	__team:AIWolfNLPRoleTeam

	def __init__(self, en:str, ja:str, team:AIWolfNLPRoleTeam) -> None:
		self.__en = en
		self.__ja = ja
		self.__team = team

	@property
	def en(self) -> str:
		"""
		Returns the role assigned at init in English.
        
        Returns:
            str: Role in English.
		"""

		return self.__en

	@property
	def ja(self) -> str:
		"""
		Returns the role assigned at init in Japanese.
        
        Returns:
            str: Role in Japanese.
		"""

		return self.__ja
	
	@property
	def team(self) -> AIWolfNLPRoleTeam:
		"""
		Returns the team of role assigned at init.
        
        Returns:
            AIWolfNLPRoleTeam: Team of role.
		"""

		return self.__team
	
	def get_translations(self) -> set:
		"""
		Get the English and Japanese of the role assigned at init.
        
        Returns:
            set: Role in English and Japanese.
		"""

		return {self.__en, self.__ja}

class AIWolfNLPRoleInfo(enum.Enum):
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
	def is_exist_role(cls, role:str) -> bool:
		is_exist = False

		for role_info in cls.__members__.values():

			if role in role_info.value.get_translations():
				is_exist = True
		
		return is_exist
	
	@classmethod
	def is_villager(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "VILLAGER" (in English) or "村人" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "VILLAGER" or "村人", False otherwise.
        """

		return role in cls.VILLAGER.value.get_translations()
	
	@classmethod
	def is_seer(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "SEER" (in English) or "占い師" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "SEER" or "占い師", False otherwise.
        """

		return role in cls.SEER.value.get_translations()
	
	@classmethod
	def is_medium(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "MEDIUM" (in English) or "霊媒師" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "MEDIUM" or "霊媒師", False otherwise.
        """

		return role in cls.MEDIUM.value.get_translations()
	
	@classmethod
	def is_bodyguard(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "BODYGUARD" (in English) or "騎士" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "BODYGUARD" or "騎士", False otherwise.
        """

		return role in cls.BODYGUARD.value.get_translations()
	
	@classmethod
	def is_werewolf(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "WEREWOLF" (in English) or "人狼" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "WEREWOLF" or "人狼", False otherwise.
        """

		return role in cls.WEREWOLF.value.get_translations()
	
	@classmethod
	def is_possessed(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "POSSESSED" (in English) or "狂人" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "POSSESSED" or "狂人", False otherwise.
        """

		return role in cls.POSSESSED.value.get_translations()
	
	@classmethod
	def is_villager_team(cls, role:str) -> Union[bool, ValueError]:
		"""
        Check if the value associated with the "role" key belongs to the Villager team.

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
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
	
	@classmethod
	def is_werewolf_team(cls, role:str) -> Union[bool, ValueError]:
		"""
        Check if the value associated with the "role" key belongs to the Werewolf team.

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
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
	
	@classmethod
	def get_villager_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "VILLAGER" role.

        Returns:
            str: The Japanese name for the "VILLAGER" role.
        """

		return cls.VILLAGER.value.ja
	
	@classmethod
	def get_seer_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "SEER" role.

        Returns:
            str: The Japanese name for the "SEER" role.
        """

		return cls.SEER.value.ja
	
	@classmethod
	def get_medium_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "MEDIUM" role.

        Returns:
            str: The Japanese name for the "MEDIUM" role.
        """		

		return cls.MEDIUM.value.ja
	
	@classmethod
	def get_werewolf_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "WEREWOLF" role.

        Returns:
            str: The Japanese name for the "WEREWOLF" role.
        """

		return cls.WEREWOLF.value.ja
	
	@classmethod
	def get_possessed_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "POSSESSED" role.

        Returns:
            str: The Japanese name for the "POSSESSED" role.
        """

		return cls.POSSESSED.value.ja