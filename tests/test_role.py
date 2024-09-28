from typing import Union
from aiwolf_nlp_common.role import AIWolfNLPRole
from AIWolfNLAgentPython.player.villager import Villager
from AIWolfNLAgentPython.player.seer import Seer
from AIWolfNLAgentPython.player.werewolf import Werewolf
from AIWolfNLAgentPython.player.possessed import Possessed

def check_is_role(agent:Union[Villager,Seer,Werewolf,Possessed], is_villager:bool=False, is_seer:bool=False,
                  is_werewolf:bool=False, is_possessed:bool=False) -> None:

    if is_villager:
        assert AIWolfNLPRole.is_villager(role=agent.role)
    else:
        assert not AIWolfNLPRole.is_villager(role=agent.role)
    
    if is_seer:
        assert AIWolfNLPRole.is_seer(role=agent.role)
    else:
        assert not AIWolfNLPRole.is_seer(role=agent.role)
    
    if is_werewolf:
        assert AIWolfNLPRole.is_werewolf(role=agent.role)
    else:
        assert not AIWolfNLPRole.is_werewolf(role=agent.role)
    
    if is_possessed:
        assert AIWolfNLPRole.is_possessed(role=agent.role)
    else:
        assert not AIWolfNLPRole.is_possessed(role=agent.role)


def test_exist_role(role_num_map) -> None:
    for role in role_num_map.keys():
        assert AIWolfNLPRole.is_exist_role(role=role)
    
    not_exist_role = ["ABC", "Villager", "ROLE"]

    for role in not_exist_role:
        assert not AIWolfNLPRole.is_exist_role(role=role)

def test_is_villager(agent_villager:Villager) -> None:
    check_is_role(agent=agent_villager, is_villager=True)

def test_is_seer(agent_seer:Seer) -> None:
    check_is_role(agent=agent_seer, is_seer=True)

def test_is_werewolf(agent_werewolf:Werewolf) -> None:
    check_is_role(agent=agent_werewolf, is_werewolf=True)

def test_is_possessed(agent_possessed:Possessed) -> None:
    check_is_role(agent=agent_possessed, is_possessed=True)