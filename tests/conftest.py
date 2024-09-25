import pytest
import json

@pytest.fixture
def initialize_json() -> dict:
    initialize_json = """{"request":"INITIALIZE","gameInfo":{"day":0,"agent":"Agent[01]","voteList":[],"latestVoteList":[],"attackVoteList":[],"latestAttackVoteList":[],"talkList":[],"whisperList":[],"statusMap":{"Agent[01]":"ALIVE","Agent[02]":"ALIVE","Agent[03]":"ALIVE","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[01]":"VILLAGER"},"remainTalkMap":{"Agent[01]":5,"Agent[02]":5,"Agent[03]":5,"Agent[04]":5,"Agent[05]":5},"remainWhisperMap":{"Agent[04]":5},"existingRoleList":["POSSESSED","SEER","VILLAGER","WEREWOLF"],"lastDeadAgentList":[]},"gameSetting":{"roleNumMap":{"ANY":0,"FREEMASON":0,"FOX":0,"POSSESSED":1,"BODYGUARD":0,"MEDIUM":0,"VILLAGER":2,"WEREWOLF":1,"SEER":1},"maxTalk":5,"maxTalkTurn":20,"maxWhisper":5,"maxWhisperTurn":20,"maxSkip":0,"isEnableNoAttack":false,"isVoteVisible":false,"isTalkOnFirstDay":true,"responseTimeout":6000,"actionTimeout":3000,"maxRevote":0,"maxAttackRevote":0,"isEnableRoleRequest":false,"playerNum":5}}"""
    return json.loads(initialize_json)