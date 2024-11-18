import enum


class Day(enum.Enum):
    GREETING_DAY = 0

    @classmethod
    def is_greeting_day(cls, day: int) -> bool:
        return day == cls.GREETING_DAY
