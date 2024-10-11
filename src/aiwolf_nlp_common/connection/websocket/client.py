import websocket
import configparser
from aiwolf_nlp_common.connection import Connection

class Websocket_Client(Connection):

    __uri_prefix:str = "ws://"

    def __init__(self, inifile: configparser.ConfigParser) -> None:
        websocket.enableTrace(traceable=False)
        self.socket = websocket.WebSocket()
        self.uri = inifile.get("websocket","uri")
    
    def connect(self) -> None:
        self.socket.connect(self.__uri_prefix + self.uri)
    
    def receive(self) -> list | RuntimeError:
        return super().receive(socket=self.socket)
    
    def send(self, message: str) -> None:
        return super().send(socket=self.socket, message=message)
    
    def close(self) -> None:
        self.socket.close()
    
