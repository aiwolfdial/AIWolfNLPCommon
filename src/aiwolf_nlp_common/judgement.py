import enum


class Judgement(enum.Enum):
    HUMAN = "HUMAN"
    WEREWOLF = "WEREWOLF"

    @classmethod
    def is_human(cls, result: str) -> bool:
        return result in {cls.HUMAN, cls.HUMAN.value}

    is_white = is_human

    @classmethod
    def is_werewolf(cls, result: str) -> bool:
        return result in {cls.WEREWOLF, cls.WEREWOLF.value}

    is_black = is_werewolf
