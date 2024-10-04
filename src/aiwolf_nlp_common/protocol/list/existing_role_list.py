"""This method is used to define a class for storing “existingRoleList” information."""

from aiwolf_nlp_common.role import AIWolfNLPRoleInfo


class ExistingRoleList(list):
    """List extension class for storing “existingRoleList” information."""

    def set_received_info(self, set_list: dict) -> None:
        """Stores information sent from the game server in class variables.

        Args:
            set_list (dict): Information on “existingRoleList” sent from the game server.
        """
        self.clear()

        if len(set_list) == 0:
            return

        for role in set_list:
            set_role = AIWolfNLPRoleInfo.VILLAGER

            if AIWolfNLPRoleInfo.is_villager(role=role):
                set_role = AIWolfNLPRoleInfo.VILLAGER
            elif AIWolfNLPRoleInfo.is_seer(role=role):
                set_role = AIWolfNLPRoleInfo.SEER
            elif AIWolfNLPRoleInfo.is_medium(role=role):
                set_role = AIWolfNLPRoleInfo.MEDIUM
            elif AIWolfNLPRoleInfo.is_possessed(role=role):
                set_role = AIWolfNLPRoleInfo.POSSESSED
            elif AIWolfNLPRoleInfo.is_werewolf(role=role):
                set_role = AIWolfNLPRoleInfo.WEREWOLF

            self.append(set_role)
