from aiwolf_nlp_common.divine import Divine

class DivineResult:
    day:int
    agent:str
    target:str
    result:Divine

    def __init__(self, day:int, agent:str, target:str, result:str) -> None:
        self.day = day
        self.agent = agent
        self.target = target
        self.result = result

    @classmethod
    def initialize_from_json(cls, value: dict) -> "DivineResult":
        return cls(
            day=value["day"],
            agent=value["agent"],
            target=value["target"],
            result=value["result"],
        )