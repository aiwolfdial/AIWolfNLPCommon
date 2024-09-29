import enum

class AIWolfNLPRoleTeam():
	__en:str
	__ja:str

	def __init__(self, en:str, ja:str) -> None:
		self.__en = en
		self.__ja = ja
	
	@property
	def en(self) -> str:
		"""
		Returns the role team assigned at init in English.
        
        Returns:
            str: Role in English.
		"""

		return self.__en

	@property
	def ja(self) -> str:
		"""
		Returns the role team assigned at init in Japanese.
        
        Returns:
            str: Role in Japanese.
		"""

		return self.__ja

class AIWolfNLPRoleTeamInfo(enum.Enum):
	VILLAGER_TEAM = AIWolfNLPRoleTeam(en="VILLAGER", ja="村人陣営")
	WEREWOLF_TEAM = AIWolfNLPRoleTeam(en="WEREWOLF", ja="人狼陣営")
	FOX_TEAM = AIWolfNLPRoleTeam(en="FOX", ja="妖狐陣営")
	ANY_TEAM = AIWolfNLPRoleTeam(en="ANY", ja="?陣営")