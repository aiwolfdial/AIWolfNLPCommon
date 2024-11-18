from typing import Union

import pytest
from AIWolfNLAgentPython.player.possessed import Possessed
from AIWolfNLAgentPython.player.seer import Seer
from AIWolfNLAgentPython.player.villager import Villager
from AIWolfNLAgentPython.player.werewolf import Werewolf

from aiwolf_nlp_common.role.role import RoleInfo


def check_is_role(
    agent: Union[Villager, Seer, Werewolf, Possessed],
    is_villager: bool = False,
    is_seer: bool = False,
    is_werewolf: bool = False,
    is_possessed: bool = False,
) -> None:
    if is_villager:
        assert RoleInfo.is_villager(role=agent.role)
    else:
        assert not RoleInfo.is_villager(role=agent.role)

    if is_seer:
        assert RoleInfo.is_seer(role=agent.role)
    else:
        assert not RoleInfo.is_seer(role=agent.role)

    if is_werewolf:
        assert RoleInfo.is_werewolf(role=agent.role)
    else:
        assert not RoleInfo.is_werewolf(role=agent.role)

    if is_possessed:
        assert RoleInfo.is_possessed(role=agent.role)
    else:
        assert not RoleInfo.is_possessed(role=agent.role)


def check_is_team(
    agent: Union[Villager, Seer, Werewolf, Possessed],
    is_villager: bool = False,
    is_seer: bool = False,
    is_werewolf: bool = False,
    is_possessed: bool = False,
) -> None:
    if is_villager or is_seer:
        assert RoleInfo.is_villager_team(role=agent.role)
    else:
        assert not RoleInfo.is_villager_team(role=agent.role)

    if is_werewolf or is_possessed:
        assert RoleInfo.is_werewolf_team(role=agent.role)
    else:
        assert not RoleInfo.is_werewolf_team(role=agent.role)


def test_exist_role(role_num_map) -> None:
    for role in role_num_map.keys():
        assert RoleInfo.is_exist_role(role=role)

    not_exist_role = ["ABC", "Villager", "ROLE"]

    for role in not_exist_role:
        assert not RoleInfo.is_exist_role(role=role)

    assert not RoleInfo.is_exist_role("Villager")
    assert RoleInfo.is_exist_role("VILLAGER")
    assert RoleInfo.is_exist_role(RoleInfo.VILLAGER)
    assert RoleInfo.is_exist_role(RoleInfo.VILLAGER.value)


def test_villager(agent_villager: Villager) -> None:
    check_is_role(agent=agent_villager, is_villager=True)
    check_is_team(agent=agent_villager, is_villager=True)

    agent_villager.role = RoleInfo.get_villager_ja()
    check_is_role(agent=agent_villager, is_villager=True)


def test_is_seer(agent_seer: Seer) -> None:
    check_is_role(agent=agent_seer, is_seer=True)
    check_is_team(agent=agent_seer, is_seer=True)

    agent_seer.role = RoleInfo.get_seer_ja()
    check_is_role(agent=agent_seer, is_seer=True)


def test_is_werewolf(agent_werewolf: Werewolf) -> None:
    check_is_role(agent=agent_werewolf, is_werewolf=True)
    check_is_team(agent=agent_werewolf, is_werewolf=True)

    agent_werewolf.role = RoleInfo.get_werewolf_ja()
    check_is_role(agent=agent_werewolf, is_werewolf=True)


def test_is_possessed(agent_possessed: Possessed) -> None:
    check_is_role(agent=agent_possessed, is_possessed=True)
    check_is_team(agent=agent_possessed, is_possessed=True)

    agent_possessed.role = RoleInfo.get_possessed_ja()
    check_is_role(agent=agent_possessed, is_possessed=True)
