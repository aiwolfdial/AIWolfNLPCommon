from aiwolf_nlp_common.role import AIWolfNLPRole
from AIWolfNLAgentPython.player.villager import Villager

def test_exist_role(role_num_map) -> None:
    for role in role_num_map.keys():
        assert AIWolfNLPRole.is_exist_role(role=role)
    
    not_exist_role = ["ABC", "Villager", "ROLE"]

    for role in not_exist_role:
        assert not AIWolfNLPRole.is_exist_role(role=role)

def test_is_villager(agent_villager:Villager) -> None:
    AIWolfNLPRole.is_seer(role=agent_villager.role)