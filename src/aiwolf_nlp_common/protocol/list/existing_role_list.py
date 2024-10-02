from aiwolf_nlp_common.role import AIWolfNLPRoleInfo

class ExistingRoleList(list):
    
    def set_received_info(self, set_list:dict) -> None:
        self.clear()

        if len(set_list) == 0:
            return
        
        for role in set_list:
            set_role = AIWolfNLPRoleInfo.VILLAGER

            if AIWolfNLPRoleInfo.is_villager(role=role):
                set_role = AIWolfNLPRoleInfo.VILLAGER
            elif AIWolfNLPRoleInfo.is_seer(role=role):
                set_role = AIWolfNLPRoleInfo.SEER
            elif AIWolfNLPRoleInfo.is_medium(role=role):
                set_role = AIWolfNLPRoleInfo.MEDIUM
            elif AIWolfNLPRoleInfo.is_possessed(role=role):
                set_role = AIWolfNLPRoleInfo.POSSESSED
            elif AIWolfNLPRoleInfo.is_werewolf(role=role):
                set_role = AIWolfNLPRoleInfo.WEREWOLF

            self.append(set_role)