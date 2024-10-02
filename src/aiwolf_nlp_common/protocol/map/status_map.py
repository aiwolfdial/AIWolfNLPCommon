from __future__ import annotations

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
    
    def __hash__(self) -> int:
        return hash(self.agent)
    
    def __eq__(self, value: object) -> bool:
        return self.agent == value.agent and self.status.value == value.status.value

class StatusMap(set):

    def change_status(self, agent:str) -> None | ValueError:

        if not agent in self:
            raise ValueError(agent + " does not exist in this set.")
        
        prev_status = None
        set_status = None

        for elem in self:
            if elem.agent == agent:
                prev_status = elem.status
        
        if Status.is_alive(status=prev_status.value):
            set_status = Status.DEAD.value
        else:
            set_status = Status.ALIVE.value
        
        self.remove(agent)
        self.add(AgentStatus(agent=agent, status=set_status))

    def set_alive(self, agent:str) -> None:
        self.add(AgentStatus(agent=agent, status=Status.ALIVE.value))
    
    def set_dead(self, agent:str) -> None:
        self.add(AgentStatus(agent=agent, status=Status.DEAD.value))

    def set_received_info(self, set_map:dict) -> None:
        self.clear()

        if len(set_map) == 0:
            return
        
        for agent in set_map.keys():
            add_elem = AgentStatus(agent=agent, status=set_map[agent])
            self.add(add_elem)