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

    def set_received_info(self, set_list: list) -> None:
        """Stores information sent from the game server in class variables.

        Args:
            set_list (list): Information on “voteList” sent from the game server.
        """
        self.clear()

        if len(set_list) == 0:
            return

        for vote_info in set_list:
            add_elem = VoteInfo(
                agent=vote_info["agent"], day=vote_info["day"], target=vote_info["target"]
            )
            self.append(add_elem)
