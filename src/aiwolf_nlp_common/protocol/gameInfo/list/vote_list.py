"""This method is used to define a class for storing “voteList” information."""


class VoteInfo:
    """Class for defining elements of “voteList”."""

    agent: int
    day: int
    target: int

    def __init__(self, agent: int, day: int, target: int) -> None:
        """Initialize “VoteInfo”.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.
            day (int): Date of statement.
            target (str): Target agent name, such as “Agent[xx]”.
        """
        self.agent = agent
        self.day = day
        self.target = target

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “VoteInfo”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if the all values are the same., False otherwise.
        """
        if value is None or not isinstance(value, VoteInfo):
            return False
        return self.agent == value.agent and self.day == value.day and self.target == value.target


class VoteList(list):
    """List extension class for storing “voteList” information."""

    @classmethod
    def initialize_from_json(cls, set_list: list) -> "VoteList":
        """Initializes a VoteList instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method creates a new instance of the VoteList class and populates it with
        VoteInfo objects based on the provided list of vote information. Each item in the
        input list should be a dictionary containing "agent", "day", and "target" keys,
        representing the vote details.

        Args:
            set_list (list): Information on "voteList" sent from the game server.
                Each element is expected to be a dictionary with the following structure:
                - "agent" (int): The agent who voted.
                - "day" (int): The day the vote was cast.
                - "target" (int): The agent who was targeted by the vote.

        Returns:
            VoteList: A new VoteList instance populated with VoteInfo objects created
            from the input data.
        """
        instance = cls()

        for vote_info in set_list:
            add_elem = VoteInfo(
                agent=vote_info["agent"], day=vote_info["day"], target=vote_info["target"]
            )
            instance.append(add_elem)
        
        return instance
