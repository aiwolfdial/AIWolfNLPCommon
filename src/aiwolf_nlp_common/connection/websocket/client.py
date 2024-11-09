from __future__ import annotations

import configparser

import websocket

from aiwolf_nlp_common.connection import Connection


class WebSocketClient(Connection):
    __uri_prefix: str = "ws://"
    __uri_suffix: str = "/ws"

    def __init__(self, inifile: configparser.ConfigParser) -> None:
        super().__init__(inifile=inifile)
        websocket.enableTrace(traceable=False)
        self.socket = websocket.WebSocket()
        self.uri = inifile.get("websocket", "uri")

    def connect(self) -> None:
        self.socket.connect(self.__uri_prefix + self.uri + self.__uri_suffix)

    def receive(self) -> list:
        response: str = self.socket.recv()
        return Connection.split_receive_info(receive=response, is_include_newline=False)

    def send(self, message: str) -> None:
        return super().send(socket=self.socket, message=message)

    def close(self) -> None:
        self.socket.close()
