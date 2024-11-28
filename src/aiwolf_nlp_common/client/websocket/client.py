from __future__ import annotations

import websocket

from aiwolf_nlp_common.client import Client


class WebSocketClient(Client):
    def __init__(self, url: str) -> None:
        super().__init__()
        websocket.enableTrace(traceable=False)
        self.socket = websocket.WebSocket()
        self.url = url

    def connect(self) -> None:
        self.socket.connect(self.url)

    def receive(self) -> list[str]:
        resp = self.socket.recv()
        resp_str = ""
        if isinstance(resp, (bytes, bytearray, memoryview)):
            resp_str = bytes(resp).decode(self.encode)
        else:
            resp_str = resp
        return Client.split_receives(receive=resp_str, include_newline=False)

    def send(self, req: str) -> None:
        if not req.endswith("\n"):
            req += "\n"
        self.socket.send(req)

    def close(self) -> None:
        self.socket.close()
