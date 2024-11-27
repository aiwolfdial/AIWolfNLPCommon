from __future__ import annotations

from .judgement_result import JudgementResult


class DivineResult(JudgementResult):
    def __init__(self, value: dict | None = None) -> None:
        super().__init__(value)
