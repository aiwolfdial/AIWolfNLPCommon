
class VoteInfo():
    agent:int
    day:int
    target:int

    def __init__(self, agent:int, day:int, target:int) -> None:
        self.agent = agent
        self.day = day
        self.target = target
    
    def __eq__(self, value: object) -> bool:
        return self.agent == value.agent and self.day == value.day and self.target == value.target

class VoteList(list):

    def set_received_info(self, set_list:list) -> None:
        self.clear()

        if len(set_list) == 0:
            return
        
        for vote_info in set_list:
            add_elem = VoteInfo(agent=vote_info["agent"], day=vote_info["day"], target=vote_info["target"])
            self.append(add_elem)