import enum
from typing import Literal

class Status(enum.Enum):
    ALIVE = "ALIVE"
    DEAD = "DEAD"

    @classmethod
    def is_alive(cls, status:str) -> bool:
        return status == cls.ALIVE.value

class AgentStatus():
    agent:str
    status:Literal[Status.ALIVE, Status.DEAD]

    def __init__(self, agent:str, status:str) -> None:
        self.agent = agent
        self.status = Status.ALIVE if Status.is_alive(status=status) else Status.DEAD

class StatusMap(set):

    def set_received_info(self, set_map:dict) -> None:
        self.clear()

        if len(set_map) == 0:
            return
        
        for agent in set_map.keys():
            add_elem = AgentStatus(agent=agent, status=set_map[agent])
            self.add(add_elem)