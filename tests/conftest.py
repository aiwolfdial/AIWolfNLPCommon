import json
import re

import pytest

from aiwolf_nlp_common import util

# from AIWolfNLAgentPython.player.agent import Agent
# from AIWolfNLAgentPython.player.possessed import Possessed
# from AIWolfNLAgentPython.player.seer import Seer
# from AIWolfNLAgentPython.player.villager import Villager
# from AIWolfNLAgentPython.player.werewolf import Werewolf


@pytest.fixture
def name_str() -> str:
    return """{"request": "NAME"}"""


@pytest.fixture
def name_json(name_str) -> dict:
    return json.loads(name_str)


@pytest.fixture
def initialize_str() -> str:
    return """{"request":"INITIALIZE","info":{"statusMap":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[01]":"WEREWOLF"},"remainTalkMap":{},"remainWhisperMap":{},"day":0,"agent":"Agent[01]"},"setting":{"roleNumMap":{"BODYGUARD":0,"MEDIUM":0,"POSSESSED":1,"SEER":1,"VILLAGER":2,"WEREWOLF":1},"playerNum":5,"maxTalk":3,"maxTalkTurn":15,"maxWhisper":3,"maxWhisperTurn":15,"maxSkip":3,"isEnableNoAttack":true,"isVoteVisible":true,"isTalkOnFirstDay":true,"responseTimeout":90000,"actionTimeout":60000,"maxRevote":1,"maxAttackRevote":1}}"""


@pytest.fixture
def initialize_json(initialize_str) -> dict:
    return json.loads(initialize_str)


@pytest.fixture
def daily_initialize_str() -> str:
    return """{"request":"DAILY_INITIALIZE","gameInfo":{"day":0,"agent":"Agent[01]","voteList":[],"latestVoteList":[],"attackVoteList":[],"latestAttackVoteList":[],"talkList":[],"whisperList":[],"statusMap":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[01]":"VILLAGER"},"remainTalkMap":{"Agent[01]":5,"Agent[02]":5,"Agent[03]":5,"Agent[04]":5,"Agent[05]":5},"remainWhisperMap":{"Agent[04]":5},"existingRoleList":["POSSESSED","SEER","VILLAGER","WEREWOLF"],"lastDeadAgentList":[]},"gameSetting":{"roleNumMap":{"ANY":0,"FREEMASON":0,"FOX":0,"POSSESSED":1,"BODYGUARD":0,"MEDIUM":0,"VILLAGER":2,"WEREWOLF":1,"SEER":1},"maxTalk":5,"maxTalkTurn":20,"maxWhisper":5,"maxWhisperTurn":20,"maxSkip":0,"isEnableNoAttack":false,"isVoteVisible":false,"isTalkOnFirstDay":true,"responseTimeout":6000,"actionTimeout":3000,"maxRevote":0,"maxAttackRevote":0,"isEnableRoleRequest":false,"playerNum":5}}"""


@pytest.fixture
def daily_initialize_json(daily_initialize_str) -> dict:
    return json.loads(daily_initialize_str)


@pytest.fixture
def talk_str() -> str:
    return """{"request":"TALK","talkHistory":[{"idx":0,"day":0,"turn":0,"agent":"Agent[03]","text":">>Agent[04] Agent[04]は他の運び屋と違い、占い師に人狼判定を出されていて、人狼判定を占いに出していないと報告されています！","skip":false,"over":false},{"idx":1,"day":0,"turn":0,"agent":"Agent[01]","text":">>Agent[05] そう。ボクがこの村の占い師なのさ。","skip":false,"over":false}],"whisperHistory":[]}"""


@pytest.fixture
def talk_json(talk_str) -> dict:
    return json.loads(talk_str)


@pytest.fixture
def daily_finish_str() -> str:
    return """{"request":"DAILY_FINISH","talkHistory":[{"idx":24,"day":0,"turn":4,"agent":"Agent[04]","text":"安心してください！　Agent[05]が人狼か？と聞かれてもYESとはいいません！　イエス、というだけです！データバンクにアクセスしてみた結果占いCOしていないと報告されています！","skip":false,"over":false},{"idx":25,"day":0,"turn":5,"agent":"Agent[05]","text":"Over","skip":false,"over":true},{"idx":26,"day":0,"turn":5,"agent":"Agent[04]","text":"Over","skip":false,"over":true},{"idx":27,"day":0,"turn":5,"agent":"Agent[03]","text":"Over","skip":false,"over":true},{"idx":28,"day":0,"turn":5,"agent":"Agent[01]","text":"Over","skip":false,"over":true},{"idx":29,"day":0,"turn":5,"agent":"Agent[02]","text":"Over","skip":false,"over":true}],"whisperHistory":[]}"""


@pytest.fixture
def daily_finish_json(daily_finish_str) -> dict:
    return json.loads(daily_finish_str)


@pytest.fixture
def divine_str() -> str:
    return """{"request":"DIVINE","talkHistory":[],"whisperHistory":[]}"""


@pytest.fixture
def divine_json(divine_str) -> dict:
    return json.loads(divine_str)


@pytest.fixture
def vote_str() -> str:
    return """{"request":"VOTE","talkHistory":[],"whisperHistory":[]}"""


@pytest.fixture
def vote_json(vote_str) -> dict:
    return json.loads(vote_str)


@pytest.fixture
def attack_str() -> str:
    return """{"request":"ATTACK","gameInfo":{"day":2,"agent":"Agent[04]","executedAgent":"Agent[01]","latestExecutedAgent":"Agent[03]","attackedAgent":"Agent[02]","voteList":[],"latestVoteList":[],"attackVoteList":[{"day":1,"agent":"Agent[04]","target":"Agent[02]"}],"latestAttackVoteList":[],"talkList":[{"idx":17,"day":2,"turn":5,"agent":"Agent[04]","text":"Over","skip":false,"over":true}],"whisperList":[],"statusMap":{"Agent[01]":"DEAD","Agent[02]":"DEAD","Agent[03]":"DEAD","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[04]":"WEREWOLF"},"remainTalkMap":{"Agent[03]":0,"Agent[04]":0,"Agent[05]":5},"remainWhisperMap":{"Agent[04]":5},"existingRoleList":["POSSESSED","SEER","VILLAGER","WEREWOLF"],"lastDeadAgentList":["Agent[02]"]}}"""


@pytest.fixture
def attack_json(attack_str) -> dict:
    return json.loads(attack_str)


@pytest.fixture
def finish_str() -> str:
    return """{"request":"FINISH","gameInfo":{"day":3,"agent":"Agent[01]","executedAgent":"Agent[03]","voteList":[],"latestVoteList":[],"attackVoteList":[],"latestAttackVoteList":[],"talkList":[],"whisperList":[],"statusMap":{"Agent[01]":"DEAD","Agent[02]":"DEAD","Agent[03]":"DEAD","Agent[04]":"ALIVE","Agent[05]":"DEAD"},"roleMap":{"Agent[01]":"VILLAGER","Agent[02]":"POSSESSED","Agent[03]":"VILLAGER","Agent[04]":"WEREWOLF","Agent[05]":"SEER"},"remainTalkMap":{"Agent[04]":5},"remainWhisperMap":{"Agent[04]":5},"existingRoleList":["POSSESSED","SEER","VILLAGER","WEREWOLF"],"lastDeadAgentList":["Agent[05]"]}}"""


@pytest.fixture
def finish_json(finish_str) -> dict:
    return json.loads(finish_str)


def json_fix(json_str: str) -> str:
    json_str = json_str.replace("'", '"')
    json_str = re.sub('[a-zA-Z]"[a-zA-Z]', "'", json_str)
    json_str = json_str.replace("False", '"False"')
    json_str = json_str.replace("True", '"True"')

    return json_str


@pytest.fixture
def role_num_map() -> dict:
    role_json = """{'request': 'INITIALIZE', 'gameInfo': {'day': 0, 'agent': 'Agent[02]', 'voteList': [], 'latestVoteList': [], 'attackVoteList': [], 'latestAttackVoteList': [], 'talkList': [], 'whisperList': [], 'statusMap': {'Agent[01]': 'ALIVE', 'Agent[02]': 'ALIVE', 'Agent[03]': 'ALIVE', 'Agent[04]': 'ALIVE', 'Agent[05]': 'ALIVE'}, 'roleMap': {'Agent[02]': 'VILLAGER'}, 'remainTalkMap': {'Agent[01]': 5, 'Agent[02]': 5, 'Agent[03]': 5, 'Agent[04]': 5, 'Agent[05]': 5}, 'remainWhisperMap': {'Agent[05]': 5}, 'existingRoleList': ['POSSESSED', 'SEER', 'VILLAGER', 'WEREWOLF'], 'lastDeadAgentList': []}, 'gameSetting': {'roleNumMap': {'SEER': 1, 'FOX': 0, 'ANY': 0, 'WEREWOLF': 1, 'MEDIUM': 0, 'POSSESSED': 1, 'VILLAGER': 2, 'BODYGUARD': 0, 'FREEMASON': 0}, 'maxTalk': 5, 'maxTalkTurn': 20, 'maxWhisper': 5, 'maxWhisperTurn': 20, 'maxSkip': 0, 'isEnableNoAttack': False, 'isVoteVisible': False, 'isTalkOnFirstDay': True, 'responseTimeout': 120000, 'actionTimeout': 1200000, 'maxRevote': 0, 'maxAttackRevote': 0, 'isEnableRoleRequest': False, 'playerNum': 5}}\n"""
    role_json = json_fix(json_str=role_json)
    role_json = json.loads(role_json)

    return role_json["gameSetting"]["roleNumMap"]


@pytest.fixture
def seer_text() -> str:
    text = """{'request': 'INITIALIZE', 'gameInfo': {'day': 0, 'agent': 'Agent[03]', 'voteList': [], 'latestVoteList': [], 'attackVoteList': [], 'latestAttackVoteList': [], 'talkList': [], 'whisperList': [], 'statusMap': {'Agent[01]': 'ALIVE', 'Agent[02]': 'ALIVE', 'Agent[03]': 'ALIVE', 'Agent[04]': 'ALIVE', 'Agent[05]': 'ALIVE'}, 'roleMap': {'Agent[03]': 'SEER'}, 'remainTalkMap': {'Agent[01]': 5, 'Agent[02]': 5, 'Agent[03]': 5, 'Agent[04]': 5, 'Agent[05]': 5}, 'remainWhisperMap': {'Agent[05]': 5}, 'existingRoleList': ['POSSESSED', 'SEER', 'VILLAGER', 'WEREWOLF'], 'lastDeadAgentList': []}, 'gameSetting': {'roleNumMap': {'SEER': 1, 'FOX': 0, 'ANY': 0, 'WEREWOLF': 1, 'MEDIUM': 0, 'POSSESSED': 1, 'VILLAGER': 2, 'BODYGUARD': 0, 'FREEMASON': 0}, 'maxTalk': 5, 'maxTalkTurn': 20, 'maxWhisper': 5, 'maxWhisperTurn': 20, 'maxSkip': 0, 'isEnableNoAttack': False, 'isVoteVisible': False, 'isTalkOnFirstDay': True, 'responseTimeout': 120000, 'actionTimeout': 1200000, 'maxRevote': 0, 'maxAttackRevote': 0, 'isEnableRoleRequest': False, 'playerNum': 5}}\n"""
    return json_fix(json_str=text)


@pytest.fixture
def seer_json(seer_text) -> dict:
    return json.loads(seer_text)


@pytest.fixture
def villager_text() -> str:
    text = """{'request': 'INITIALIZE', 'gameInfo': {'day': 0, 'agent': 'Agent[02]', 'voteList': [], 'latestVoteList': [], 'attackVoteList': [], 'latestAttackVoteList': [], 'talkList': [], 'whisperList': [], 'statusMap': {'Agent[01]': 'ALIVE', 'Agent[02]': 'ALIVE', 'Agent[03]': 'ALIVE', 'Agent[04]': 'ALIVE', 'Agent[05]': 'ALIVE'}, 'roleMap': {'Agent[02]': 'VILLAGER'}, 'remainTalkMap': {'Agent[01]': 5, 'Agent[02]': 5, 'Agent[03]': 5, 'Agent[04]': 5, 'Agent[05]': 5}, 'remainWhisperMap': {'Agent[05]': 5}, 'existingRoleList': ['POSSESSED', 'SEER', 'VILLAGER', 'WEREWOLF'], 'lastDeadAgentList': []}, 'gameSetting': {'roleNumMap': {'SEER': 1, 'FOX': 0, 'ANY': 0, 'WEREWOLF': 1, 'MEDIUM': 0, 'POSSESSED': 1, 'VILLAGER': 2, 'BODYGUARD': 0, 'FREEMASON': 0}, 'maxTalk': 5, 'maxTalkTurn': 20, 'maxWhisper': 5, 'maxWhisperTurn': 20, 'maxSkip': 0, 'isEnableNoAttack': False, 'isVoteVisible': False, 'isTalkOnFirstDay': True, 'responseTimeout': 120000, 'actionTimeout': 1200000, 'maxRevote': 0, 'maxAttackRevote': 0, 'isEnableRoleRequest': False, 'playerNum': 5}}\n"""

    return json_fix(json_str=text)


@pytest.fixture
def villager_json(villager_text) -> dict:
    return json.loads(villager_text)


@pytest.fixture
def possessed_text() -> str:
    text = """{'request': 'INITIALIZE', 'gameInfo': {'day': 0, 'agent': 'Agent[01]', 'voteList': [], 'latestVoteList': [], 'attackVoteList': [], 'latestAttackVoteList': [], 'talkList': [], 'whisperList': [], 'statusMap': {'Agent[01]': 'ALIVE', 'Agent[02]': 'ALIVE', 'Agent[03]': 'ALIVE', 'Agent[04]': 'ALIVE', 'Agent[05]': 'ALIVE'}, 'roleMap': {'Agent[01]': 'POSSESSED'}, 'remainTalkMap': {'Agent[01]': 5, 'Agent[02]': 5, 'Agent[03]': 5, 'Agent[04]': 5, 'Agent[05]': 5}, 'remainWhisperMap': {'Agent[05]': 5}, 'existingRoleList': ['POSSESSED', 'SEER', 'VILLAGER', 'WEREWOLF'], 'lastDeadAgentList': []}, 'gameSetting': {'roleNumMap': {'SEER': 1, 'FOX': 0, 'ANY': 0, 'WEREWOLF': 1, 'MEDIUM': 0, 'POSSESSED': 1, 'VILLAGER': 2, 'BODYGUARD': 0, 'FREEMASON': 0}, 'maxTalk': 5, 'maxTalkTurn': 20, 'maxWhisper': 5, 'maxWhisperTurn': 20, 'maxSkip': 0, 'isEnableNoAttack': False, 'isVoteVisible': False, 'isTalkOnFirstDay': True, 'responseTimeout': 120000, 'actionTimeout': 1200000, 'maxRevote': 0, 'maxAttackRevote': 0, 'isEnableRoleRequest': False, 'playerNum': 5}}\n"""
    return json_fix(json_str=text)


@pytest.fixture
def possessed_json(possessed_text) -> dict:
    return json.loads(possessed_text)


@pytest.fixture
def werewolf_text() -> str:
    text = """{'request': 'INITIALIZE', 'gameInfo': {'day': 0, 'agent': 'Agent[02]', 'voteList': [], 'latestVoteList': [], 'attackVoteList': [], 'latestAttackVoteList': [], 'talkList': [], 'whisperList': [], 'statusMap': {'Agent[01]': 'ALIVE', 'Agent[02]': 'ALIVE', 'Agent[03]': 'ALIVE', 'Agent[04]': 'ALIVE', 'Agent[05]': 'ALIVE'}, 'roleMap': {'Agent[02]': 'WEREWOLF'}, 'remainTalkMap': {'Agent[01]': 5, 'Agent[02]': 5, 'Agent[03]': 5, 'Agent[04]': 5, 'Agent[05]': 5}, 'remainWhisperMap': {'Agent[02]': 5}, 'existingRoleList': ['POSSESSED', 'SEER', 'VILLAGER', 'WEREWOLF'], 'lastDeadAgentList': []}, 'gameSetting': {'roleNumMap': {'BODYGUARD': 0, 'VILLAGER': 2, 'FOX': 0, 'SEER': 1, 'WEREWOLF': 1, 'FREEMASON': 0, 'MEDIUM': 0, 'POSSESSED': 1, 'ANY': 0}, 'maxTalk': 5, 'maxTalkTurn': 20, 'maxWhisper': 5, 'maxWhisperTurn': 20, 'maxSkip': 0, 'isEnableNoAttack': False, 'isVoteVisible': False, 'isTalkOnFirstDay': True, 'responseTimeout': 120000, 'actionTimeout': 1200000, 'maxRevote': 0, 'maxAttackRevote': 0, 'isEnableRoleRequest': False, 'playerNum': 5}}\n"""
    return json_fix(json_str=text)


@pytest.fixture
def werewolf_json(werewolf_text) -> dict:
    return json.loads(werewolf_text)


@pytest.fixture
def text_file_path() -> str:
    return "tests/AIWolfNLAgentPython/res/2019071_44011_AIWolfTalkLogs.txt"


@pytest.fixture
def config_file_path() -> str:
    return "tests/AIWolfNLAgentPython/res/config.ini"


# @pytest.fixture
# def agent() -> Agent:
#     config_path = "tests/AIWolfNLAgentPython/res/config.ini"
#     inifile = util.read_config_file(config_file_path=config_path)

#     return Agent(inifile=inifile, name="test")


# @pytest.fixture
# def agent_villager(villager_text: str) -> Villager:
#     config_path = "tests/AIWolfNLAgentPython/res/config.ini"
#     inifile = util.read_config_file(config_file_path=config_path)

#     agent = Villager(inifile=inifile, name="test_villager")

#     agent.parse_info(receive=villager_text)
#     agent.get_info()
#     agent.action()

#     return agent


# @pytest.fixture
# def agent_seer(seer_text: str) -> Seer:
#     config_path = "tests/AIWolfNLAgentPython/res/config.ini"
#     inifile = util.read_config_file(config_file_path=config_path)

#     agent = Seer(inifile=inifile, name="test_seer")

#     agent.parse_info(receive=seer_text)
#     agent.get_info()
#     agent.action()

#     return agent


# @pytest.fixture
# def agent_werewolf(werewolf_text: str) -> Werewolf:
#     config_path = "tests/AIWolfNLAgentPython/res/config.ini"
#     inifile = util.read_config_file(config_file_path=config_path)

#     agent = Werewolf(inifile=inifile, name="test_werewolf")

#     agent.parse_info(receive=werewolf_text)
#     agent.get_info()
#     agent.action()

#     return agent


# @pytest.fixture
# def agent_possessed(possessed_text: str) -> Possessed:
#     config_path = "tests/AIWolfNLAgentPython/res/config.ini"
#     inifile = util.read_config_file(config_file_path=config_path)

#     agent = Possessed(inifile=inifile, name="test_possessed")

#     agent.parse_info(receive=possessed_text)
#     agent.get_info()
#     agent.action()

#     return agent
