from __future__ import annotations

import enum


class Status(enum.Enum):
    ALIVE = "ALIVE"
    DEAD = "DEAD"

    @classmethod
    def is_alive(cls, status: str | Status) -> bool:
        return status in {cls.ALIVE, cls.ALIVE.value}

    @classmethod
    def is_dead(cls, status: str | Status) -> bool:
        return status in {cls.DEAD, cls.DEAD.value}
