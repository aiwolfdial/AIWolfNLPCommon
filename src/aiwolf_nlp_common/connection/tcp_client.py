import configparser
from .tcp_connection import TCPConnection

class TCPClient(TCPConnection):
    """
       Connection method used to go to a game server waiting for a connection.
    """

    def __init__(self, inifile:configparser.ConfigParser) -> None:
        super().__init__(inifile=inifile)
        self.host = inifile.get("tcp-client","host")
        self.port = inifile.getint("tcp-client","port")

    def connect(self) -> None:
        """
        Connect to the game server based on the information in the “host” and “post” fields of the config file.
        """

        self.socket.connect((self.host,self.port))
    
    def receive(self) -> str:
        return super().receive()
    
    def send(self, message:str) -> None:
        super().send(message=message)

    def close(self) -> None:
        super().close()