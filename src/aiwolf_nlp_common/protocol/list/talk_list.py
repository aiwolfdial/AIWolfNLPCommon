from __future__ import annotations

class TalkInfo():
    agent:str
    day:int
    idx:int
    text:str
    turn:str
    skip:bool
    over:bool

    def __init__(self, agent:str, day:int, idx:int, text:str, turn:str, skip:bool, over:bool) -> None:
        self.agent = agent
        self.day = day
        self.idx = idx
        self.text = text
        self.turn = turn
        self.skip = skip
        self.over = over
    
    def __eq__(self, value: object) -> bool:
        return (self.agent == value.agent and self.day == value.day and
                self.idx == value.idx and self.text == value.text and
                self.turn == value.turn and self.skip == value.skip and
                self.over == value.over)

class TalkList(list):

    def set_received_info(self, set_list:dict) -> None:
        self.clear()

        if len(set_list) == 0:
            return
        
        for talk_info in set_list:
            add_elem = TalkInfo(agent=talk_info["agent"], day=talk_info["day"], idx=talk_info["idx"],
                                text=talk_info["text"], turn=talk_info["turn"],
                                skip=talk_info["skip"], over=talk_info["over"])
            self.append(add_elem)