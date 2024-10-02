import enum

class Status(enum.Enum):
    ALIVE = "ALIVE"
    DEAD = "DEAD"

    @classmethod
    def is_alive(cls, status:str) -> bool:
        return status == cls.ALIVE.value

class StatusMap(dict):

    def set_received_info(self, set_map:dict) -> None:
        self.clear()

        if len(set_map) == 0:
            return
        
        for agent in set_map.keys():
            status =  Status.ALIVE if Status.is_alive(status=set_map[agent]) else Status.DEAD
            self.__setitem__(agent, status)