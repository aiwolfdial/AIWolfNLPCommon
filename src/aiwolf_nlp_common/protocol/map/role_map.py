from aiwolf_nlp_common.role import AIWolfNLPRoleInfo

class RoleMap(dict):
    
    
    def set_received_info(self, set_map:dict) -> None:
        self.clear()

        if len(set_map) == 0:
            return
        
        for agent in set_map.keys():
            set_role = AIWolfNLPRoleInfo.VILLAGER

            if AIWolfNLPRoleInfo.is_villager(role=set_map[agent]):
                set_role = AIWolfNLPRoleInfo.VILLAGER
            elif AIWolfNLPRoleInfo.is_seer(role=set_map[agent]):
                set_role = AIWolfNLPRoleInfo.SEER
            elif AIWolfNLPRoleInfo.is_medium(role=set_map[agent]):
                set_role = AIWolfNLPRoleInfo.MEDIUM
            elif AIWolfNLPRoleInfo.is_possessed(role=set_map[agent]):
                set_role = AIWolfNLPRoleInfo.POSSESSED
            elif AIWolfNLPRoleInfo.is_werewolf(role=set_map[agent]):
                set_role = AIWolfNLPRoleInfo.WEREWOLF
        
            self.__setitem__(agent, set_role)