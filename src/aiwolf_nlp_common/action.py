import enum

class AIWolfNLPAction(enum.Enum):
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
	def is_initialize(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "INITIALIZE".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "INITIALIZE", False otherwise.
		"""

		return request == cls.INITIALIZE.value
	
	@classmethod
	def is_name(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "NAME".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "NAME", False otherwise.
		"""
		return request == cls.NAME.value
	
	@classmethod
	def is_role(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "ROLE".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "ROLE", False otherwise.
		"""

		return request == cls.ROLE.value
	
	@classmethod
	def is_daily_initialize(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "DAILY_INITIALIZE".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "DAILY_INITIALIZE", False otherwise.
		"""

		return request == cls.DAILY_INITIALIZE.value
	
	@classmethod
	def is_daily_finish(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "DAILY_FINISH".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "DAILY_FINISH", False otherwise.
		"""

		return request == cls.DAILY_FINISH.value
	
	@classmethod
	def is_talk(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "TALK".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "TALK", False otherwise.
		"""

		return request == cls.TALK.value
	
	@classmethod
	def is_vote(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "VOTE".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "VOTE", False otherwise.
		"""

		return request == cls.VOTE.value
	
	@classmethod
	def is_divine(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "DIVINE".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "DIVINE", False otherwise.
		"""

		return request == cls.DIVINE.value
	
	@classmethod
	def is_attack(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "ATTACK".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "ATTACK", False otherwise.
		"""

		return request == cls.ATTACK.value
	
	@classmethod
	def is_whisper(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "WHISPER".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "WHISPER", False otherwise.
		"""

		return request == cls.WHISPER.value
	
	@classmethod
	def is_finish(cls, request:str) -> bool:
		"""
			Check if the value associated with the "request" key is "FINISH".

			Args:
				request (str): The value associated with the "request" key sent from the game server.
			
			Returns:
				bool: True if the value is "FINISH", False otherwise.
		"""

		return request == cls.FINISH.value