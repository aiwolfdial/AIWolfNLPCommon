"""This module defines the basic settings and behaviors for communicating with the game server."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import configparser
    import socket

    import paramiko


class Connection:
    """A class that describes the settings and actions required to connect to the game server."""

    _encode_format: str = "utf-8"

    def __init__(self, inifile: configparser.ConfigParser) -> None:
        """Receive information from the game server and return it as a string.

        Args:
            inifile (configparser.ConfigParser):
                Config file with buffer information in [connection].
        """
        self.buffer = inifile.getint("connection", "buffer")

    def receive(self, socket: socket.socket | paramiko.channel.Channel) -> str | RuntimeError:
        """Receive information from the game server and return it as a string.

        Args:
            socket (socket.socket | paramiko.channel.Channel):
                socket that establishes the connection to the game server.

        Returns:
            str: Information is received from the game server and encoded.

        Raises:
        RuntimeError: If the connection to the game server is lost.

        """
        responses = b""

        while not self.is_json_complate(responses=responses):
            response = socket.recv(self.buffer)

            if response == b"":
                err_message = "socket connection broken"
                raise RuntimeError(err_message)

            responses += response

        return responses.decode(self._encode_format)

    def send(self, socket: socket.socket | paramiko.channel.Channel, message: str) -> None:
        """Send information to the game server with a new line.

        Args:
            socket (socket.socket | paramiko.channel.Channel):
                socket that establishes the connection to the game server.
            message (str): Information you want to send to the game server.

        """
        message += "\n"

        socket.send(message.encode(self._encode_format))

    @classmethod
    def is_json_complate(cls, responses: bytes) -> bool:
        """Confirm that the data received from the game server is in JSON format.

        Args:
            responses (bytes): Data received from the game server.

        Returns:
            bool: True if the responses format is JSON, False otherwise.

        """
        try:
            responses = responses.decode(cls._encode_format)
        except UnicodeDecodeError:
            return False

        if responses == "":
            return False

        cnt = 0

        for word in responses:
            if word == "{":
                cnt += 1
            elif word == "}":
                cnt -= 1

        return cnt == 0

    @classmethod
    def is_include_text(cls, receive_data: str) -> bool:
        """Verify that the information received from the game server is not empty.

        Args:
            receive_data (str): Information received from the game server and encoded.

        Returns:
            bool: True if the receive_data is include text, False otherwise.

        """
        return "{" in receive_data
