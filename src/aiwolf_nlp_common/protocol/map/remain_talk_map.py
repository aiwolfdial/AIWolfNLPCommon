
class AgentRemainTalk():
    agent:str
    remain_talk_number:int

    def __init__(self, agent:str, remain_talk_number:int) -> None:
        self.agent = agent
        self.remain_talk_number = remain_talk_number
    
    def __hash__(self) -> int:
        return hash(self.agent)
    
    def __eq__(self, value: object) -> bool:
        return self.agent == value.agent and self.remain_talk_number == value.remain_talk_number

class RemainTalkMap(set):

    def set_received_info(self, set_map:dict) -> None:
        self.clear()

        if len(set_map) == 0:
            return
        
        for agent in set_map.keys():
            add_elem = AgentRemainTalk(agent=agent, remain_talk_number=set_map[agent])
            self.add(add_elem)