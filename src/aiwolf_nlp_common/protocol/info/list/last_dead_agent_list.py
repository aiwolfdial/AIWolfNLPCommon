"""This method is used to define a class for storing “lastDeadAgentList” information."""


class LastDeadAgentList(list):
    """List extension class for storing “lastDeadAgentList” information."""

    @classmethod
    def initialize_from_json(cls, set_list: list) -> "LastDeadAgentList":
        """Initializes a LastDeadAgentList instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method creates a new instance of the LastDeadAgentList class and populates it with
        the agents that have died in the game. The provided list is expected to contain information
        about the last dead agents as sent from the game server.

        Args:
            set_list (list): Information on “lastDeadAgentList” sent from the game server.
                Each element in the list is expected to represent an agent that has died.

        Returns:
            LastDeadAgentList: A new LastDeadAgentList instance populated with agent information
            created from the input data.
        """
        instance = cls()

        for agent in set_list:
            instance.append(agent)

        return instance