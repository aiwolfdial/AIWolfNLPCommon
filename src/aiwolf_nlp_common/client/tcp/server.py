from __future__ import annotations

import socket

from aiwolf_nlp_common.client.client import Client


class TCPServer(Client):
    def __init__(
        self,
        host_ip: str,
        host_port: int,
    ) -> None:
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = host_ip
        self.host_port = host_port

    def connect(self) -> None:
        self.socket.bind((self.host_ip, self.host_port))
        self.socket.listen()
        self.client_socket, _ = self.socket.accept()

    def receive(self) -> str:
        resp = b""
        while not self.is_valid(resp=resp):
            raw = self.client_socket.recv(2048)
            if raw == b"":
                err_message = "socket connection broken"
                raise RuntimeError(err_message)
            resp += raw
        return resp.decode(self.encode)

    def send(self, req: str) -> None:
        if not req.endswith("\n"):
            req += "\n"
        self.client_socket.send(req.encode(self.encode))

    def close(self) -> None:
        self.client_socket.close()
