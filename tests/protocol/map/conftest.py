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
def status_map_json() -> None:
    status_map_json = """{"request":"ATTACK","gameInfo":{"day":2,"agent":"Agent[04]","executedAgent":"Agent[01]","latestExecutedAgent":"Agent[03]","attackedAgent":"Agent[02]","voteList":[],"latestVoteList":[],"attackVoteList":[{"day":1,"agent":"Agent[04]","target":"Agent[02]"}],"latestAttackVoteList":[],"talkList":[{"idx":17,"day":2,"turn":5,"agent":"Agent[04]","text":"Over","skip":false,"over":true}],"whisperList":[],"statusMap":{"Agent[01]":"DEAD","Agent[02]":"DEAD","Agent[03]":"DEAD","Agent[04]":"ALIVE","Agent[05]":"ALIVE"},"roleMap":{"Agent[04]":"WEREWOLF"},"remainTalkMap":{"Agent[03]":0,"Agent[04]":0,"Agent[05]":5},"remainWhisperMap":{"Agent[04]":5},"existingRoleList":["POSSESSED","SEER","VILLAGER","WEREWOLF"],"lastDeadAgentList":["Agent[02]"]}}"""
    return json.loads(status_map_json)
