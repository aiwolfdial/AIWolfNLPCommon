from __future__ import annotations


class JudgementResult:
    __default_day: int = -1
    __default_agent: str = "Agent[00]"
    __default_target: str = "Agent[00]"
    __default_result: str = "unknown"

    def __init__(
        self,
        day: int = __default_day,
        agent: str = __default_agent,
        target: str = __default_target,
        result: str = __default_result,
    ) -> None:
        self.day = day
        self.agent = agent
        self.target = target
        self.result = result

    @classmethod
    def initialize_from_json(cls, value: dict | None) -> "JudgementResult":
        if value is None:
            return cls()

        return cls(
            day=value["day"],
            agent=value["agent"],
            target=value["target"],
            result=value["result"],
        )

    def is_empty(self) -> bool:
        return (
            self.day == self.__default_day
            and self.agent == self.__default_agent
            and self.target == self.__default_target
            and self.result == self.__default_result
        )
