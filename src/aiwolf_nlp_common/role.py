import enum
from typing import Union

LANGUAGE = 2

ROLE_EN_POS = 1
ROLE_JA_POS = 2
IS_VILLAGER_POS = 3

class AIWolfNLPRole(enum.Enum):
	# villager team
	VILLAGER = ("VILLAGER", "村人", True)
	SEER = ("SEER", "占い師", True)
	MEDIUM = ("MEDIUM", "霊媒師", True)

	# werewolf team
	WEREWOLF = ("WEREWOLF", "人狼", False)
	POSSESSED = ("POSSESSED", "狂人", False)

	def __init__(self, en:str, ja:str, is_villagerr_team:bool) -> None:
		self.en = en
		self.ja = ja
		self.is_villagerr_team = is_villagerr_team
	
	@classmethod
	def is_exist_role(cls, role:str) -> bool:
		is_exist = False

		for role_info in cls.__members__.values():
			role_name_list = role_info.value[:LANGUAGE]

			if role in role_name_list:
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

		return role in cls.VILLAGER.value[:LANGUAGE]
	
	@classmethod
	def is_seer(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "SEER" (in English) or "占い師" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "SEER" or "占い師", False otherwise.
        """

		return role in cls.SEER.value[:LANGUAGE]
	
	@classmethod
	def is_medium(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "MEDIUM" (in English) or "霊媒師" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "MEDIUM" or "霊媒師", False otherwise.
        """

		return role in cls.MEDIUM.value[:LANGUAGE]
	
	@classmethod
	def is_werewolf(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "WEREWOLF" (in English) or "人狼" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "WEREWOLF" or "人狼", False otherwise.
        """

		return role in cls.WEREWOLF.value[:LANGUAGE]
	
	@classmethod
	def is_possessed(cls, role:str) -> bool:
		"""
        Check if the value associated with the "role" key is either "POSSESSED" (in English) or "狂人" (in Japanese).

        Args:
            request (str): The value associated with the "role" key sent from the game server.
        
        Returns:
            bool: True if the value is "POSSESSED" or "狂人", False otherwise.
        """

		return role in cls.POSSESSED.value[:LANGUAGE]
	
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
			role_name_list = role_info.value[:LANGUAGE]

			if role in role_name_list:
				return role_info.value[IS_VILLAGER_POS - 1]
	
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

		try:
			return not cls.is_villager_team(role=role)
		except ValueError as e:
			raise e
	
	@classmethod
	def get_villager_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "VILLAGER" role.

        Returns:
            str: The Japanese name for the "VILLAGER" role.
        """

		return cls.VILLAGER.value[ROLE_JA_POS]
	
	@classmethod
	def get_seer_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "SEER" role.

        Returns:
            str: The Japanese name for the "SEER" role.
        """

		return cls.SEER.value[ROLE_JA_POS]
	
	@classmethod
	def get_medium_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "MEDIUM" role.

        Returns:
            str: The Japanese name for the "MEDIUM" role.
        """		

		return cls.MEDIUM.value[ROLE_JA_POS]
	
	@classmethod
	def get_werewolf_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "WEREWOLF" role.

        Returns:
            str: The Japanese name for the "WEREWOLF" role.
        """

		return cls.WEREWOLF.value[ROLE_JA_POS]
	
	@classmethod
	def get_possessed_ja(cls) -> str:
		"""
        Retrieve the Japanese name for the "POSSESSED" role.

        Returns:
            str: The Japanese name for the "POSSESSED" role.
        """

		return cls.POSSESSED.value[ROLE_JA_POS]