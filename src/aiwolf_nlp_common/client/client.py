from __future__ import annotations

import json
import re


class Client:
    encode = "utf-8"

    def __init__(self) -> None:
        pass

    def receive(self) -> list[str] | str | None:
        pass

    def send(self, req: str) -> None:
        pass

    def close(self) -> None:
        pass

    @classmethod
    def is_valid(cls, resp: bytes) -> bool:
        try:
            resp_str = resp.decode(cls.encode)
        except UnicodeDecodeError:
            return False
        if resp_str == "":
            return False
        try:
            json.loads(resp_str)
        except ValueError:
            return False
        return True

    @classmethod
    def split_receives(cls, receive: str, *, include_newline: bool = True) -> list[str]:
        if include_newline:
            return re.findall("({.*})\n", receive)
        return re.findall("({.*})", receive)
