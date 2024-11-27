import enum


class Judgement(enum.Enum):
    HUMAN = "HUMAN"
    WEREWOLF = "WEREWOLF"

    @classmethod
    def is_human(cls, result: str) -> bool:
        return result in {cls.HUMAN, cls.HUMAN.value}

    @classmethod
    def is_werewolf(cls, result: str) -> bool:
        return result in {cls.WEREWOLF, cls.WEREWOLF.value}
