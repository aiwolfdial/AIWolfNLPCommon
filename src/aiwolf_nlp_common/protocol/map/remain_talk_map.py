"""This method is used to define a class for storing “remainTalkMap” information."""


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
            int: Result of hashing by agent name.
        """
        return hash(self.agent)

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “AgentRemainTalk”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if the all values are the same., False otherwise.
        """
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

    def set_received_info(self, set_map: dict) -> None:
        """Stores information sent from the game server in class variables.

        Args:
            set_map (map): Information on “remainTalkMap” sent from the game server.
        """
        self.clear()

        if len(set_map) == 0:
            return

        for agent in set_map:
            add_elem = AgentRemainTalkInfo(agent=agent, remain_talk_number=set_map[agent])
            self.add(add_elem)
