"""This module defines methods and settings necessary for SSH communication with the game server.

This method is used to listen for connections from the game server.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import paramiko

from aiwolf_nlp_common.connection import Connection

if TYPE_CHECKING:
    import configparser


class SSHServer(Connection):
    """Connection method used to listen for connections from the game server."""

    def __init__(self, inifile: configparser.ConfigParser, name: str) -> None:
        """Set up the information necessary to communicate with the game server.

        Args:
            inifile (configparser.ConfigParser):
                Config file with buffer information in [connection].
            name (str): Agent name.
        """
        super().__init__(inifile=inifile)
        self.ssh_config_path = inifile.get("ssh-server", "config_path")
        self.ssh_host_name = inifile.get("ssh-server", "host_name")
        self.ssh_agent_flag = inifile.getboolean("ssh-server", "ssh_agent_flag")
        self.timeout = inifile.getint("ssh-server", "timeout")
        self.ssh_remote_forward_port = self.get_ssh_port(inifile=inifile, name=name)

    def get_ssh_port(self, inifile: configparser.ConfigParser, name: str) -> int:
        """Get the setting of the port to bind to the public server from the configuration file.

        Based on the agent's name and the settings in the Config file,
            the current agent is searched for which port to listen on.
        Search from name1 to name10 at maximum.

        Args:
            inifile (configparser.ConfigParse):
                A config file that contains information about the connection to the game server
                    such as “ip” and “port”.
            name (str): Name of the agent running the program.

        Returns:
            int: Port number to listen on.

        Raises:
            ValueError: If “name” is not found in the Config file.

        """
        for i in range(1, 11, 1):
            name_str = "name" + str(i)

            if name == inifile.get("agent", name_str):
                return i - 1

        raise ValueError(name + " was not found in the Config file.")

    def read_ssh_config(self) -> paramiko.SSHConfigDict:
        """Read the Config file for the ssh connection.

        Returns:
            paramiko.SSHConfigDict: Result of parsing the Config file for ssh connections.

        """
        config_file = Path(self.ssh_config_path).expanduser()
        ssh_config = paramiko.SSHConfig()

        with Path(config_file).open("r", encoding=self._encode_format) as file:
            ssh_config.parse(file)

        return ssh_config.lookup(self.ssh_host_name)

    def set_ssh_toolkit(self) -> None:
        """Prepare for ssh connection with paramiko."""
        self.ssh_client = paramiko.SSHClient()
        self.ssh_agent = paramiko.Agent()
        self.ssh_agent_keys = self.ssh_agent.get_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def set_ssh_config(self) -> None | ValueError:
        """Configure the necessary settings for SSH connection.

        Raises:
            ValueError: If you are configured to use ssh_agent but cannot find ssh_agent.

        """
        self.config = self.read_ssh_config()
        self.ssh_pkey = None
        self.key_filename = None

        if self.ssh_agent_flag and len(self.ssh_agent_keys) > 0:
            self.ssh_pkey = self.ssh_agent_keys[0]
        elif self.ssh_agent_flag and len(self.ssh_agent_keys) == 0:
            err_message = "SSH agent does not contain any keys or the agent is not running."
            raise ValueError(err_message)

    def connect(self) -> None:
        """Connect to the remote server via SSH and wait for the game server to connect."""
        self.set_ssh_toolkit()
        self.set_ssh_config()

        self.ssh_client.connect(
            self.config["hostname"],
            username=self.config["user"],
            pkey=self.ssh_pkey,
            key_filename=self.config.get("identityfile"),
            timeout=self.timeout,
        )

        self.ssh_remote_forward()

    def ssh_remote_forward(self) -> None:
        """Remote forward to the specified port on the ssh-connected server."""
        self.transport = self.ssh_client.get_transport()
        parts = self.config["remoteforward"][self.ssh_remote_forward_port].split()
        remote_port = int(parts[0])

        self.transport.request_port_forward(address="", port=remote_port)
        self.channel = self.transport.accept()

    def receive(self) -> str:
        """Receive information from the game server and return it as a string.

        Returns:
            str: Information is received from the game server and encoded.

        Raises:
            RuntimeError: If the connection to the game server is lost.

        """
        return super().receive(socket=self.channel)

    def send(self, message: str) -> None:
        """Send information to the game server with a new line.

        Args:
            message (str): Information you want to send to the game server.

        """
        return super().send(socket=self.channel, message=message)

    def close(self) -> None:
        """Close the socket."""
        self.ssh_client.close()
        self.channel.close()
