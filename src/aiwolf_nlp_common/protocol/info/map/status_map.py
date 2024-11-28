from __future__ import annotations

from aiwolf_nlp_common.status import Status


class AgentStatus:
    def __init__(self, agent: str, status: str) -> None:
        self.__agent = agent
        self.__status = Status.ALIVE if Status.is_alive(status=status) else Status.DEAD

    def __hash__(self) -> int:
        return hash((self.agent, self.status.value))

    def __eq__(self, value: object) -> bool:
        if value is None or not isinstance(value, self.__class__):
            return NotImplemented
        return self.agent == value.agent and self.status.value == value.status.value

    def __lt__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return NotImplemented
        return self.__agent < value.__agent

    def __str__(self) -> str:
        return f"{self.__agent} is {self.status.value}"

    @property
    def agent(self) -> str:
        return self.__agent

    @property
    def status(self) -> Status:
        return self.__status


class StatusMap(set):
    def __str__(self) -> str:
        output: str = f"[{self.__class__.__name__}]"
        if self.is_empty():
            return output + "\nNo Result Available"
        return output + "\n".join(str(elem) for elem in sorted(self))

    def __init__(self, value: dict | None = None) -> None:
        super().__init__()
        if value is not None:
            for agent, status in value.items():
                self.add(AgentStatus(agent=agent, status=status))

    def is_empty(self) -> bool:
        return len(self) == 0

    def reverse_status(self, agent: str) -> None:
        prev_alive = AgentStatus(agent=agent, status=Status.ALIVE.value)
        prev_dead = AgentStatus(agent=agent, status=Status.DEAD.value)
        if prev_alive not in self and prev_dead not in self:
            raise ValueError(agent, "is a name that does not exist.")
        if prev_alive in self:
            self.remove(prev_alive)
            self.add(prev_dead)
        else:
            self.remove(prev_dead)
            self.add(prev_alive)

    def set_alive(self, agent: str) -> None:
        self.add(AgentStatus(agent=agent, status=Status.ALIVE.value))

    def set_dead(self, agent: str) -> None:
        self.add(AgentStatus(agent=agent, status=Status.DEAD.value))

    def get_alive_agent_list(self) -> list:
        return sorted(
            [status.agent for status in self if Status.is_alive(status=status.status)],
        )

    def get_dead_agent_list(self) -> list:
        return sorted(
            [status.agent for status in self if Status.is_dead(status=status.status)],
        )
