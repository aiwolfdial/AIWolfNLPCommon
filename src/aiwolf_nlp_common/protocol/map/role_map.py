from aiwolf_nlp_common.role import AIWolfNLPRoleInfo

from typing import Literal

class AgentRole():
    agent:str
    role:Literal[AIWolfNLPRoleInfo.VILLAGER, AIWolfNLPRoleInfo.SEER,
                 AIWolfNLPRoleInfo.MEDIUM, AIWolfNLPRoleInfo.POSSESSED,
                 AIWolfNLPRoleInfo.WEREWOLF]

    def __init__(self, agent:str, role:str) -> None:
        self.agent = agent

        if AIWolfNLPRoleInfo.is_villager(role=role):
            self.role = AIWolfNLPRoleInfo.VILLAGER
        elif AIWolfNLPRoleInfo.is_seer(role=role):
            self.role = AIWolfNLPRoleInfo.SEER
        elif AIWolfNLPRoleInfo.is_medium(role=role):
            self.role = AIWolfNLPRoleInfo.MEDIUM
        elif AIWolfNLPRoleInfo.is_possessed(role=role):
            self.role = AIWolfNLPRoleInfo.POSSESSED
        elif AIWolfNLPRoleInfo.is_werewolf(role=role):
            self.role = AIWolfNLPRoleInfo.WEREWOLF
        else:
            self.role = AIWolfNLPRoleInfo.ANY
    
    def __hash__(self) -> int:
        return hash(self.agent)
    
    def __eq__(self, value: object) -> bool:
        return self.agent == value.agent and self.role == value.role

class RoleMap(set):
    
    
    def set_received_info(self, set_map:dict) -> None:
        self.clear()

        if len(set_map) == 0:
            return
        
        for agent in set_map.keys():
            add_elem = AgentRole(agent=agent, role=set_map[agent])
            self.add(add_elem)