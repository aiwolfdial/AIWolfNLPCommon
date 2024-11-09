"""This module defines methods and settings necessary for TCP communication with the game server.

This method is used to listen for connections from the game server.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .tcp_connection import TCPConnection

if TYPE_CHECKING:
    import configparser


class TCPServer(TCPConnection):
    """Connection method used to listen for connections from the game server."""

    def __init__(self, inifile: configparser.ConfigParser, name: str) -> None:
        """Set up the information necessary to communicate with the game server.

        Args:
            inifile (configparser.ConfigParser):
                Config file with buffer information in [connection].
            name (str): Agent name.
        """
        super().__init__(inifile=inifile)
        self.host_ip = inifile.get("tcp-server", "ip")
        self.host_port = self.get_host_port(inifile=inifile, name=name)
        self.socket.bind((self.host_ip, self.host_port))

    def get_host_port(self, inifile: configparser.ConfigParser, name: str) -> int:
        """BSet up information to wait for the game server.

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
                port_str = "port" + str(i)
                return inifile.getint("tcp-server", port_str)

        raise ValueError(name + " was not found in the Config file.")

    def connect(self) -> None:
        """Wait for connections from the game server."""
        self.socket.listen()
        self.client_socket, self.client_address = self.socket.accept()

    def receive(self) -> str | RuntimeError:
        """Receive information from the game server and return it as a string.

        Returns:
            str: Information is received from the game server and encoded.

        Raises:
            RuntimeError: If the connection to the game server is lost.

        """
        return super().receive()

    def send(self, message: str) -> None:
        """Send information to the game server with a new line.

        Args:
            message (str): Information you want to send to the game server.

        """
        return super().send(message=message)

    def close(self) -> None:
        """Close the socket."""
        self.client_socket.close()
        super().close()
