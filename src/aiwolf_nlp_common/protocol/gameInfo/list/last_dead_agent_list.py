"""This method is used to define a class for storing “lastDeadAgentList” information."""


class LastDeadAgentList(list):
    """List extension class for storing “lastDeadAgentList” information."""

    def set_received_info(self, set_list: list) -> None:
        """Stores information sent from the game server in class variables.

        Args:
            set_list (list): Information on “lastDeadAgentList” sent from the game server.
        """
        self.clear()

        if len(set_list) == 0:
            return

        for agent in set_list:
            self.append(agent)
