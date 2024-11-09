"""This module defines methods and settings necessary for TCP communication with the game server."""

from __future__ import annotations

import socket
from typing import TYPE_CHECKING

from aiwolf_nlp_common.connection import Connection

if TYPE_CHECKING:
    import configparser


class TCPConnection(Connection):
    """This class specifies the info and actions needed for a TCP connection to the game server."""

    def __init__(self, inifile: configparser.ConfigParser) -> None:
        """Set up the information necessary to communicate with the game server.

        Args:
            inifile (configparser.ConfigParser):
                Config file with buffer information in [connection].
        """
        super().__init__(inifile)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def receive(self) -> str:
        """Receive information from the game server and return it as a string.

        Returns:
            str: Information is received from the game server and encoded.

        Raises:
            RuntimeError: If the connection to the game server is lost.

        """
        return super().receive(socket=self.socket)

    def send(self, message: str) -> None:
        """Send information to the game server with a new line.

        Args:
            message (str): Information you want to send to the game server.

        """
        return super().send(socket=self.socket, message=message)

    def close(self) -> None:
        """Close the socket."""
        self.socket.close()
