import configparser
from typing import Union
from .tcp_connection import TCPConnection

class TCPServer(TCPConnection):
    """
       Connection method used to listen for connections from the game server.
    """
    
    def __init__(self, inifile:configparser.ConfigParser, name:str) -> None:
        super().__init__(inifile=inifile)
        self.host_ip = inifile.get("tcp-server","ip")
        self.host_port = self.get_host_port(inifile=inifile, name=name)
        self.socket.bind((self.host_ip,self.host_port))
    
    def get_host_port(self, inifile:configparser.ConfigParser, name:str) -> Union[int, ValueError]:
        """
        Based on the agent's name and the settings in the Config file, the current agent is searched for which port to listen on.
        Search from name1 to name10 at maximum.

        Args:
            inifile (configparser.ConfigParse): IA config file that contains information about the connection to the game server, such as “ip” and “port”.
            name (str): Name of the agent running the program.
        
        Returns:
            int: Port number to listen on.
        
        Raises:
            ValueError: If “name” is not found in the Config file.
        """

        for i in range(1, 11, 1):
            name_str = "name" + str(i)

            if name == inifile.get("agent",name_str):
                port_str = "port" + str(i)
                return inifile.getint("tcp-server",port_str)
        
        raise ValueError(name + " was not found in the Config file.")
    
    def connect(self) -> None:
        """
            Wait for connections from the game server based on the "ip" and “port” description in the config file.
        """

        print("server listening...",end="\t")
        print("ip:" + self.host_ip + " port:" + str(self.host_port))
        self.socket.listen()
        self.client_socket, self.address = self.socket.accept()
    
    def receive(self) -> str:
        return super().receive()
    
    def send(self, message: str) -> None:
        return super().send(message=message)
    
    def close(self):
        self.client_socket.close()
        super().close()