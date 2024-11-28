from __future__ import annotations

from typing import TYPE_CHECKING

import paramiko

from aiwolf_nlp_common.client import Client

if TYPE_CHECKING:
    from pathlib import Path


class SSHClient(Client):
    def __init__(  # noqa: PLR0913
        self,
        ssh_config_path: Path,
        ssh_host_name: str,
        ssh_username: str,
        ssh_key_filename: str,
        use_ssh_agent: bool,  # noqa: FBT001
        timeout: int,
        remote_forward_port: int,
    ) -> None:
        super().__init__()
        self.ssh_config_path = ssh_config_path
        self.ssh_host_name = ssh_host_name
        self.ssh_username = ssh_username
        self.ssh_key_filename = ssh_key_filename
        self.use_ssh_agent = use_ssh_agent
        self.timeout = timeout
        self.remote_forward_port = remote_forward_port

    def read_ssh_config(self) -> paramiko.SSHConfigDict:
        config_file = self.ssh_config_path.expanduser()
        ssh_config = paramiko.SSHConfig()
        with config_file.open("r", encoding=self.encode) as file:
            ssh_config.parse(file)
        return ssh_config.lookup(self.ssh_host_name)

    def set_ssh_toolkit(self) -> None:
        self.ssh_client = paramiko.SSHClient()
        self.ssh_agent = paramiko.Agent()
        self.ssh_agent_keys = self.ssh_agent.get_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def set_ssh_config(self) -> None | ValueError:
        self.config = self.read_ssh_config()
        self.ssh_pkey = None
        self.key_filename = None
        if self.use_ssh_agent and len(self.ssh_agent_keys) > 0:
            self.ssh_pkey = self.ssh_agent_keys[0]
        elif self.use_ssh_agent and len(self.ssh_agent_keys) == 0:
            err_message = (
                "ssh-agent is not available or no keys are available in ssh-agent"
            )
            raise ValueError(err_message)

    def connect(self) -> None:
        self.set_ssh_toolkit()
        self.set_ssh_config()
        self.ssh_client.connect(
            hostname=self.ssh_host_name,
            username=self.ssh_username,
            pkey=self.ssh_pkey,
            key_filename=self.ssh_key_filename,
            timeout=self.timeout,
        )
        self.transport = self.ssh_client.get_transport()
        self.ssh_remote_forward()

    def ssh_remote_forward(self) -> None:
        if self.transport is None:
            err_message = "transport is not connected"
            raise RuntimeError(err_message)
        self.transport.request_port_forward(address="", port=self.remote_forward_port)
        self.channel = self.transport.accept()

    def receive(self) -> str:
        if self.channel is None:
            err_message = "channel is not connected"
            raise RuntimeError(err_message)
        resp = b""
        while not self.is_valid(resp=resp):
            raw = self.channel.recv(2048)
            if raw == b"":
                err_message = "socket connection broken"
                raise RuntimeError(err_message)
            resp += raw
        return resp.decode(self.encode)

    def send(self, req: str) -> None:
        if not req.endswith("\n"):
            req += "\n"
        if self.channel is not None:
            self.channel.send(bytes(req, self.encode))

    def close(self) -> None:
        self.ssh_client.close()
        if self.channel is not None:
            self.channel.close()
