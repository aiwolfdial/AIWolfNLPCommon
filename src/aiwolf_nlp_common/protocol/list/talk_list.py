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

    def __str__(self) -> str:
        return f"index:{self.idx}, {self.agent}: {self.text}"

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

    def __str__(self) -> str:
        output: str = f"[{self.__class__.__name__}]"

        if self.is_empty():
            return output + "\nNo Result Available"

        elem: TalkInfo
        for elem in self:
            output += "\n" + elem.__str__()

        return output

    @classmethod
    def initialize_from_json(cls, set_list: list | None) -> "TalkList":
        """Initializes a TalkList instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method creates a new instance of the TalkList class and populates it with
        TalkInfo objects based on the provided list of talk information. Each item in the
        input list is expected to be a dictionary containing details about a talk, including
        the agent who spoke, the day of the talk, and various attributes of the talk itself.

        Args:
            set_list (list): Information on “talkList” sent from the game server.
                Each element is expected to be a dictionary with the following structure:
                - "agent" (int): The agent who spoke.
                - "day" (int): The day the talk occurred.
                - "idx" (int): The index of the talk in the sequence.
                - "text" (str): The text of the talk.
                - "turn" (int): The turn number when the talk occurred.
                - "skip" (bool): Indicates if the talk was skipped.
                - "over" (bool): Indicates if the talk is over.

        Returns:
            TalkList: A new TalkList instance populated with TalkInfo objects created
            from the input data.
        """
        instance = cls()

        if set_list is None:
            return instance

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
            instance.append(add_elem)

        return instance

    def is_empty(self) -> bool:
        """Check if the object is empty.

        This method returns True if the object has no elements (i.e., its length is 0),
        and False otherwise.

        Returns:
            bool: True if the object is empty, False otherwise.
        """
        return len(self) == 0
