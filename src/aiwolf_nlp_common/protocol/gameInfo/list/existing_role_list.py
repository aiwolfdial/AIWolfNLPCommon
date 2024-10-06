"""This method is used to define a class for storing “existingRoleList” information."""

from aiwolf_nlp_common.role import AIWolfNLPRoleInfo


class ExistingRoleList(list):
    """List extension class for storing “existingRoleList” information."""

    def set_received_info(self, set_list: list) -> None:
        """Stores information sent from the game server in class variables.

        Args:
            set_list (list): Information on “existingRoleList” sent from the game server.
        """
        self.clear()

        if len(set_list) == 0:
            return

        for role in set_list:
            set_role = AIWolfNLPRoleInfo.get_role_info(role=role)
            self.append(set_role)
