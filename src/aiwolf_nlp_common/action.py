from __future__ import annotations

import enum


class Action(enum.Enum):
    INITIALIZE = "INITIALIZE"
    NAME = "NAME"
    ROLE = "ROLE"
    DAILY_INITIALIZE = "DAILY_INITIALIZE"
    DAILY_FINISH = "DAILY_FINISH"
    TALK = "TALK"
    VOTE = "VOTE"
    DIVINE = "DIVINE"
    ATTACK = "ATTACK"
    WHISPER = "WHISPER"
    FINISH = "FINISH"

    @classmethod
    def is_initialize(cls, request: str | Action) -> bool:
        return request in {cls.INITIALIZE, cls.INITIALIZE.value}

    @classmethod
    def is_name(cls, request: str | Action) -> bool:
        return request in {cls.NAME, cls.NAME.value}

    @classmethod
    def is_role(cls, request: str | Action) -> bool:
        return request in {cls.ROLE, cls.ROLE.value}

    @classmethod
    def is_daily_initialize(cls, request: str | Action) -> bool:
        return request in {cls.DAILY_INITIALIZE, cls.DAILY_INITIALIZE.value}

    @classmethod
    def is_daily_finish(cls, request: str | Action) -> bool:
        return request in {cls.DAILY_FINISH, cls.DAILY_FINISH.value}

    @classmethod
    def is_talk(cls, request: str | Action) -> bool:
        return request in {cls.TALK, cls.TALK.value}

    @classmethod
    def is_vote(cls, request: str | Action) -> bool:
        return request in {cls.VOTE, cls.VOTE.value}

    @classmethod
    def is_divine(cls, request: str | Action) -> bool:
        return request in {cls.DIVINE, cls.DIVINE.value}

    @classmethod
    def is_attack(cls, request: str | Action) -> bool:
        return request in {cls.ATTACK, cls.ATTACK.value}

    @classmethod
    def is_whisper(cls, request: str | Action) -> bool:
        return request in {cls.WHISPER, cls.WHISPER.value}

    @classmethod
    def is_finish(cls, request: str | Action) -> bool:
        return request in {cls.FINISH, cls.FINISH.value}
