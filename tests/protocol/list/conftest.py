import json
import re

import pytest


def json_fix(json_str: str) -> str:
    json_str = json_str.replace("'", '"')
    json_str = re.sub('[a-zA-Z]"[a-zA-Z]', "'", json_str)
    json_str = json_str.replace("False", '"False"')
    json_str = json_str.replace("True", '"True"')
    json_str = json_str.replace("None", '"None"')

    return json_str


@pytest.fixture
def vote_list_json() -> dict:
    vote_list_json = """{'gameInfo': {'agent': 4, 'attackVoteList': [], 'attackedAgent': -1, 'cursedFox': -1, 'day': 3, 'divineResult': None, 'englishTalkList': [], 'executedAgent': 1, 'existingRoleList': ['POSSESSED', 'SEER', 'VILLAGER', 'WEREWOLF'], 'guardedAgent': -1, 'lastDeadAgentList': [], 'latestAttackVoteList': [], 'latestExecutedAgent': -1, 'latestVoteList': [], 'mediumResult': None, 'remainTalkMap': {'2': 10, '5': 10}, 'remainWhisperMap': {}, 'roleMap': {'1': 'WEREWOLF', '2': 'SEER', '3': 'POSSESSED', '4': 'VILLAGER', '5': 'VILLAGER'}, 'statusMap': {'1': 'DEAD', '2': 'ALIVE', '3': 'DEAD', '4': 'DEAD', '5': 'ALIVE'}, 'talkList': [], 'voteList': [{'agent': 1, 'day': 2, 'target': 2}, {'agent': 2, 'day': 2, 'target': 1}, {'agent': 5, 'day': 2, 'target': 1}], 'whisperList': []}, 'gameSetting': None, 'request': 'FINISH', 'talkHistory': None, 'whisperHistory': None}\n"""
    return json.loads(json_fix(json_str=vote_list_json))


@pytest.fixture
def talk_list_json() -> dict:
    talk_list_json = """{"request":"ATTACK","gameInfo":{"day":2,"agent":"Agent[04]","executedAgent":"Agent[01]","latestExecutedAgent":"Agent[03]","attackedAgent":"Agent[02]","voteList":[],"latestVoteList":[],"attackVoteList":[{"day":1,"agent":"Agent[04]","target":"Agent[02]"}],"latestAttackVoteList":[],"talkList":[{"idx":17,"day":2,"turn":5,"agent":"Agent[04]","text":"Over","skip":false,"over":true},{"idx":18,"day":2,"turn":5,"agent":"Agent[04]","text":"Skip","skip":true,"over":false},{"idx":19,"day":2,"turn":5,"agent":"Agent[04]","text":"Test","skip":false,"over":false}],"whisperList":[],"statusMap":{"Agent[01]":"DEAD","Agent[02]":"DEAD","Agent[03]":"DEAD","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[04]":"WEREWOLF"},"remainTalkMap":{"Agent[03]":0,"Agent[04]":0,"Agent[05]":5},"remainWhisperMap":{"Agent[04]":5},"existingRoleList":["POSSESSED","SEER","VILLAGER","WEREWOLF"],"lastDeadAgentList":["Agent[02]"]}}"""
    return json.loads(talk_list_json)


@pytest.fixture
def existing_role_list_json() -> dict:
    existing_role_list_json = """{'gameInfo': {'agent': 4, 'attackVoteList': [], 'attackedAgent': -1, 'cursedFox': -1, 'day': 2, 'divineResult': None, 'englishTalkList': [], 'executedAgent': 3, 'existingRoleList': ['POSSESSED', 'SEER', 'VILLAGER', 'WEREWOLF'], 'guardedAgent': -1, 'lastDeadAgentList': [4], 'latestAttackVoteList': [], 'latestExecutedAgent': -1, 'latestVoteList': [], 'mediumResult': None, 'remainTalkMap': {'1': 10, '2': 10, '5': 10}, 'remainWhisperMap': {}, 'roleMap': {'4': 'VILLAGER'}, 'statusMap': {'1': 'ALIVE', '2': 'ALIVE', '3': 'DEAD', '4': 'DEAD', '5': 'ALIVE'}, 'talkList': [], 'voteList': [{'agent': 1, 'day': 1, 'target': 3}, {'agent': 2, 'day': 1, 'target': 4}, {'agent': 3, 'day': 1, 'target': 2}, {'agent': 4, 'day': 1, 'target': 3}, {'agent': 5, 'day': 1, 'target': 4}], 'whisperList': []}, 'gameSetting': {'enableNoAttack': False, 'enableNoExecution': False, 'enableRoleRequest': False, 'maxAttackRevote': 1, 'maxRevote': 1, 'maxSkip': 0, 'maxTalk': 10, 'maxTalkTurn': 20, 'maxWhisper': 10, 'maxWhisperTurn': 20, 'playerNum': 5, 'randomSeed': 1710509577819, 'roleNumMap': {'MEDIUM': 0, 'WEREWOLF': 1, 'VILLAGER': 2, 'FOX': 0, 'SEER': 1, 'FREEMASON': 0, 'POSSESSED': 1, 'BODYGUARD': 0}, 'talkOnFirstDay': True, 'timeLimit': 6000000, 'validateUtterance': False, 'votableInFirstDay': False, 'voteVisible': True, 'whisperBeforeRevote': False}, 'request': 'DAILY_INITIALIZE', 'talkHistory': None, 'whisperHistory': None}\n"""
    return json.loads(existing_role_list_json)


@pytest.fixture
def last_dead_agent_list_json() -> dict:
    last_dead_agent_list_json = """{"request":"ATTACK","gameInfo":{"day":2,"agent":"Agent[04]","executedAgent":"Agent[01]","latestExecutedAgent":"Agent[03]","attackedAgent":"Agent[02]","voteList":[],"latestVoteList":[],"attackVoteList":[{"day":1,"agent":"Agent[04]","target":"Agent[02]"}],"latestAttackVoteList":[],"talkList":[{"idx":17,"day":2,"turn":5,"agent":"Agent[04]","text":"Over","skip":false,"over":true}],"whisperList":[],"statusMap":{"Agent[01]":"DEAD","Agent[02]":"DEAD","Agent[03]":"DEAD","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[04]":"WEREWOLF"},"remainTalkMap":{"Agent[03]":0,"Agent[04]":0,"Agent[05]":5},"remainWhisperMap":{"Agent[04]":5},"existingRoleList":["POSSESSED","SEER","VILLAGER","WEREWOLF"],"lastDeadAgentList":["Agent[02]"]}}"""

    return json.loads(last_dead_agent_list_json)
