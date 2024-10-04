"""This method is used to define a class for storing “talkList” information."""

from __future__ import annotations


class TalkInfo:
    """Class for defining elements of “talkList”."""

    agent: str
    day: int
    idx: int
    text: str
    turn: str
    skip: bool
    over: bool

    def __init__(
        self, agent: str, day: int, idx: int, text: str, turn: str, *, skip: bool, over: bool
    ) -> None:
        """Initialize “TalkInfo”.

        Args:
            agent (str): Agent name, such as “Agent[xx]”.
            day (int): Date of statement.
            idx (int): Serial number of the day's remarks.
            text (str): Statement Content.
            turn (str): The serial number of that agent's statement for that day.
            skip (bool): True if the text is "Skip", False otherwise.
            over (bool): True if the text is "Over", False otherwise.
        """
        self.agent = agent
        self.day = day
        self.idx = idx
        self.text = text
        self.turn = turn
        self.skip = skip
        self.over = over

    def is_skip(self) -> bool:
        """Check if the content of the text is “Skip”.

        Returns:
            bool: True if the text is "Skip", False otherwise.
        """
        return self.skip

    def is_over(self) -> bool:
        """Check if the content of the text is “Over”.

        Returns:
            bool: True if the text is "Over", False otherwise.
        """
        return self.over

    def __eq__(self, value: object) -> bool:
        """Comparison method for making comparisons in “TalkInfo”.

        Args:
            value (object): Comparison object.

        Returns:
            bool: True if the all values are the same., False otherwise.
        """
        if value is None or not isinstance(value, TalkInfo):
            return False

        return (
            self.agent == value.agent
            and self.day == value.day
            and self.idx == value.idx
            and self.text == value.text
            and self.turn == value.turn
            and self.skip == value.skip
            and self.over == value.over
        )


class TalkList(list):
    """List extension class for storing “talkList” information."""

    def set_received_info(self, set_list: list) -> None:
        """Stores information sent from the game server in class variables.

        Args:
            set_list (list): Information on “talkList” sent from the game server.
        """
        self.clear()

        if len(set_list) == 0:
            return

        for talk_info in set_list:
            add_elem = TalkInfo(
                agent=talk_info["agent"],
                day=talk_info["day"],
                idx=talk_info["idx"],
                text=talk_info["text"],
                turn=talk_info["turn"],
                skip=talk_info["skip"],
                over=talk_info["over"],
            )
            self.append(add_elem)
