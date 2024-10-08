"""This method is used to define a class for storing “existingRoleList” information."""

from aiwolf_nlp_common.role import RoleInfo


class ExistingRoleList(list):
    """List extension class for storing “existingRoleList” information."""

    @classmethod
    def initialize_from_json(cls, set_list: list) -> "ExistingRoleList":
        """Initializes an ExistingRoleList instance from JSON data received from the game server.

        This docstring was created by a generative AI.
        This method creates a new instance of the ExistingRoleList class and populates it with
        role information based on the provided list of existing roles. Each element in the input
        list is expected to represent a role identifier, which is used to retrieve the corresponding
        role information.

        Args:
            set_list (list): Information on “existingRoleList” sent from the game server.
                Each element is expected to be a role identifier that can be used to obtain
                role information.

        Returns:
            ExistingRoleList: A new ExistingRoleList instance populated with role information
            created from the input data.
        """
        instance = cls()

        for role in set_list:
            set_role = RoleInfo.get_role_info(role=role)
            instance.append(set_role)

        return instance
