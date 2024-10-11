"""This module defines methods and settings necessary for TCP communication with the game server.

This module is used when going to connect to the game server.
"""

import configparser

from .tcp_connection import TCPConnection


class TCPClient(TCPConnection):
    """Connection method used to go to a game server waiting for a connection."""

    def __init__(self, inifile: configparser.ConfigParser) -> None:
        """Set up the information necessary to communicate with the game server.

        Args:
            inifile (configparser.ConfigParser):
                Config file with buffer information in [connection].
        """
        super().__init__(inifile=inifile)
        self.host = inifile.get("tcp-client", "host")
        self.port = inifile.getint("tcp-client", "port")

    def connect(self) -> None:
        """Connect to the game server."""
        self.socket.connect((self.host, self.port))

    def receive(self) -> str:
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
        super().send(message=message)

    def close(self) -> None:
        """Close the socket."""
        super().close()
