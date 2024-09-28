from aiwolf_nlp_common.role import AIWolfNLPRole
from AIWolfNLAgentPython.player.villager import Villager

def check_is_role(agent, is_villager:bool=False) -> None:

    if is_villager:
        assert AIWolfNLPRole.is_villager(role=agent.role)
    else:
        assert not AIWolfNLPRole.is_villager(role=agent.role)

def test_exist_role(role_num_map) -> None:
    for role in role_num_map.keys():
        assert AIWolfNLPRole.is_exist_role(role=role)
    
    not_exist_role = ["ABC", "Villager", "ROLE"]

    for role in not_exist_role:
        assert not AIWolfNLPRole.is_exist_role(role=role)

def test_is_villager(agent_villager:Villager) -> None:
    check_is_role(agent=agent_villager, is_villager=True)