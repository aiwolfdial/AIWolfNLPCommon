from __future__ import annotations

from typing import Callable

class TalkInfo():
    agent:int
    day:int
    idx:int
    text:str

    def __init__(self, agent:int, day:int, idx:int, text:str) -> None:
        self.agent = agent
        self.day = day
        self.idx = idx
        self.text = text

class TalkList(list):

    def set_received_info(self, set_list:dict) -> None:
        self.clear()

        if len(set_list) == 0:
            return
        
        for talk_info in set_list:
            add_elem = TalkInfo(agent=talk_info["agent"], day=talk_info["day"], idx=talk_info["idx"], text=talk_info["text"])
            self.append(add_elem)