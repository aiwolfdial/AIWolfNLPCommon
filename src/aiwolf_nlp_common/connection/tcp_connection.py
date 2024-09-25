import socket
import configparser
from typing import Union
from .connection import Connection

class TCPConnection(Connection):

    _encode_format:str = "utf-8"

    def __init__(self,inifile:configparser.ConfigParser) -> None:
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.buffer = inifile.getint("connection","buffer")
    
    def receive(self) -> Union[str, RuntimeError]:
        """
        Receive information from the game server and return it as a string.
        
        Returns:
            str: Information is received from the game server and encoded.
        
        Raises:
			RuntimeError: If the connection to the game server is lost.
        """

        return super().receive(socket=self.socket)
    
    def send(self, message: str) -> None:
        """
        Send information to the game server with a new line.

        Args:
            message (str): Information you want to send to the game server.
        """

        return super().send(socket=self.socket, message=message)
    
    def close(self) -> None:
        """
        Close the socket.
        """

        self.socket.close()
    
    @classmethod
    def is_json_complate(cls, responses:bytes) -> bool:
        """
        Confirm that the data received from the game server is in JSON format.

        Args:
            responses (bytes): Data received from the game server.
        
        Returns:
            bool: True if the responses format is JSON, False otherwise.
        """

        try:
            responses = responses.decode(cls._encode_format)
        except:
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
    def is_include_text(cls, receive_data:str) -> bool:
        """
        Verify that the information received from the game server is not empty.

        Args:
            receive_data (str): Information received from the game server and encoded.
        
        Returns:
            bool: True if the receive_data is include text, False otherwise.
        """

        return "{" in receive_data