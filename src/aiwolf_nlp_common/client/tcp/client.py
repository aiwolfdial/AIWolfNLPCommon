import socket

from aiwolf_nlp_common.client.client import Client


class TCPClient(Client):
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
        self.socket.connect((self.host_ip, self.host_port))

    def receive(self) -> str:
        resp = b""
        while not self.is_valid(resp=resp):
            raw = self.socket.recv(2048)
            if raw == b"":
                err_message = "socket connection broken"
                raise RuntimeError(err_message)
            resp += raw
        return resp.decode(self.encode)

    def send(self, req: str) -> None:
        if not req.endswith("\n"):
            req += "\n"
        self.socket.send(req.encode(self.encode))

    def close(self) -> None:
        self.socket.close()
