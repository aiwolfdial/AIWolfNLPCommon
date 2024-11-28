from __future__ import annotations

from aiwolf_nlp_common.role import Role, RoleInfo


class AgentRole:
    __agent: str
    __role: Role

    def __init__(self, agent: str, role: str) -> None:
        self.__agent = agent
        self.__role = RoleInfo.get_role_info(role=role)

    def __hash__(self) -> int:
        return hash((self.agent, self.role.en))

    def __eq__(self, value: object) -> bool:
        if value is None or not isinstance(value, AgentRole):
            return False
        return self.agent == value.agent and self.role == value.role

    def __lt__(self, value: object) -> bool:
        if value is None or not isinstance(value, self.__class__):
            return NotImplemented
        return self.__agent < value.__agent

    def __str__(self) -> str:
        return f"{self.__agent} is {self.__role.en}"

    @property
    def agent(self) -> str:
        return self.__agent

    @property
    def role(self) -> Role:
        return self.__role


class RoleMap(set):
    def __str__(self) -> str:
        output: str = f"[{self.__class__.__name__}]"
        if self.is_empty():
            return output + "\nNo Result Available"
        return output + "\n" + "\n".join(str(elem) for elem in sorted(self))

    def __init__(self, value: dict | None = None) -> None:
        super().__init__()
        if value is not None:
            for agent, role in value.items():
                self.add(AgentRole(agent=agent, role=role))

    def get_role(self, agent: str) -> Role:
        for agent_role in self:
            if agent_role.agent == agent:
                return agent_role.role
        raise ValueError(agent, "is a name that does not exist.")

    def is_empty(self) -> bool:
        return len(self) == 0
