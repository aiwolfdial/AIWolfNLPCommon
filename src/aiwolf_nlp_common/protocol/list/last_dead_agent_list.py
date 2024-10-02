
class LastDeadAgentList(list):
    
    def set_received_info(self, set_list:dict) -> None:
        self.clear()

        if len(set_list) == 0:
            return
        
        for agent in set_list:
            self.append(agent)