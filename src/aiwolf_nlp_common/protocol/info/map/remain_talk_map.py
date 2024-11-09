"""This method is used to define a class for storing “remainTalkMap” information."""

from __future__ import annotations


class AgentRemainTalkInfo:
    """Class for defining elements of “remainTalkMap”."""

    __agent: str
    __remain_talk_number: int

    def __init__(self, agent: str, remain_talk_number: int) -> None:
        """Initialize “AgentRemainTalk”.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.
            remain_talk_number (int): Remaining number of utterances.
        """
        self.__agent = agent
        self.__remain_talk_number = remain_talk_number

    def __hash__(self) -> int:
        """Comparison method for making comparisons in “AgentRemainTalk”.

        Returns:
            int: Result of hashing by agent name and remain_talk_number.
        """
        return hash((self.agent, self.remain_talk_number))

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “AgentRemainTalk”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if the all values are the same., False otherwise.
        """
        if value is None or not isinstance(value, AgentRemainTalkInfo):
            return False

        return self.agent == value.agent and self.remain_talk_number == value.remain_talk_number

    @property
    def agent(self) -> str:
        """Gets the agent's name.

        This property returns the agent's name in the format "Agent[xx]",
        where "xx" is the agent's identifier.

        Returns:
            str: Agent name, such as “Agent[xx]”.
        """
        return self.__agent

    @property
    def remain_talk_number(self) -> int:
        """Gets the agent's remaining number of utterances.

        This property returns the number of remaining utterances that
        the agent can make.

        Returns:
            int: The remaining number of utterances.
        """
        return self.__remain_talk_number


class RemainTalkMap(set):
    """Set extension class for storing “remainTalkMap” information."""

    @classmethod
    def initialize_from_json(cls, set_map: dict) -> RemainTalkMap:
        """Initializes a RemainTalkMap instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method creates a new instance of the RemainTalkMap class and populates it with
        information about the remaining talk numbers for each agent. The provided dictionary
        maps agent identifiers to their respective remaining talk numbers.

        Args:
            set_map (dict): Information on “remainTalkMap” sent from the game server.
                Each key in the dictionary is an agent identifier, and the corresponding
                value is the number of remaining talks for that agent.

        Returns:
            RemainTalkMap: A new RemainTalkMap instance populated with AgentRemainTalkInfo
            objects created from the input data.
        """
        instance = cls()

        for agent in set_map:
            add_elem = AgentRemainTalkInfo(agent=agent, remain_talk_number=set_map[agent])
            instance.add(add_elem)

        return instance

    def is_empty(self) -> bool:
        """Check if the object is empty.

        This method returns True if the object has no elements (i.e., its length is 0),
        and False otherwise.

        Returns:
            bool: True if the object is empty, False otherwise.
        """
        return len(self) == 0

    def get_agent_remain_talk_number(self, agent: str) -> int:
        """Retrieve the remaining talk number of a specified agent.

        This docstring was created by a generative AI.
        This method searches for the remaining talk count associated
        with the given agent name. If the agent is found, it returns
        the corresponding remaining talk number; otherwise, it raises
        a ValueError.

        Args:
            agent (str): The name of the agent, formatted as “Agent[xx]”.

        Returns:
            int: The remaining talk number of the specified agent.

        Raises:
            ValueError: If the specified agent name does not exist
            in the current context.
        """
        for agent_remain_info in self:
            if agent_remain_info.agent == agent:
                return agent_remain_info.remain_talk_number

        raise ValueError(agent + " is a name that does not exist.")
