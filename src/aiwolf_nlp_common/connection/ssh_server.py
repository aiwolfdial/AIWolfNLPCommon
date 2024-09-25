import os
import paramiko
import configparser
from typing import Union
from .connection import Connection

class SSHServer(Connection):
    """
    A connection method used when a game server connects to a public server via ssh and waits for connections from the game server there.
    """

    def __init__(self,inifile:configparser.ConfigParser, name:str) -> None:
        super().__init__(inifile=inifile)
        self.ssh_config_path = inifile.get("ssh-server","config_path")
        self.ssh_host_name = inifile.get("ssh-server","host_name")
        self.ssh_agent_flag = inifile.getboolean("ssh-server","ssh_agent_flag")
        self.timeout = inifile.getint("ssh-server","timeout")
        self.ssh_remoteforward_port = self.get_ssh_port(inifile=inifile, name=name)

    def get_ssh_port(self, inifile:configparser.ConfigParser, name:str) -> Union[int, ValueError]:
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
                return i - 1
        
        raise ValueError(name + " was not found in the Config file.")
    
    def read_ssh_config(self) -> paramiko.SSHConfigDict:
        """
        Read the Config file for the ssh connection.
        
        Returns:
            paramiko.SSHConfigDict: Result of parsing the Config file for ssh connections.
        """

        config_file = os.path.expanduser(self.ssh_config_path)
        ssh_config = paramiko.SSHConfig()
        ssh_config.parse(open(config_file, 'r'))

        return ssh_config.lookup(self.ssh_host_name)
    
    def set_ssh_toolkit(self) -> None:
        """
        Prepare for ssh connection with paramiko.
        """

        self.ssh_client = paramiko.SSHClient()
        self.ssh_agent = paramiko.Agent()
        self.ssh_agent_keys = self.ssh_agent.get_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def set_ssh_config(self) -> Union[None, ValueError]:
        """
        Configure settings to connect to the game server based on the Config file for the ssh connection.

        Raises:
            ValueError: If you are configured to use ssh_agent but cannot find the information registered in ssh_agent.       
        """

        self.config = self.read_ssh_config()
        self.ssh_pkey = None
        self.key_filename = None
        
        if self.ssh_agent_flag and len(self.ssh_agent_keys) > 0:
            self.ssh_pkey = self.ssh_agent_keys[0]
        elif self.ssh_agent_flag and len(self.ssh_agent_keys) == 0:
            raise ValueError("SSH agent does not contain any keys or the agent is not running.")
    
    def connect(self, remote_foward_flag = True) -> None:
        """
        Make an ssh connection to the server where the game server is published.

        Args:
            remote_foward_flag (bool): True Execute a remote forward., False Do not execute remote forwarding.
        """

        self.set_ssh_toolkit()
        self.set_ssh_config()
        
        self.ssh_client.connect(self.config["hostname"], username=self.config["user"], pkey=self.ssh_pkey, key_filename=self.config.get("identityfile"), timeout=self.timeout)

        if remote_foward_flag:
            self.ssh_remote_forward()
    
    def ssh_remote_forward(self) -> None:
        """
        Remote forward to the specified port on the ssh-connected server.
        """

        self.transport = self.ssh_client.get_transport()
        parts = self.config["remoteforward"][self.ssh_remoteforward_port].split()
        remote_port = int(parts[0])
        local_port = int(parts[1].split(":")[1])

        self.transport.request_port_forward(address="",port=remote_port)
        self.channel = self.transport.accept()
    
    def receive(self) -> Union[str, RuntimeError]:
        return super().receive(socket=self.channel)
    
    def send(self, message: str) -> None:
        return super().send(socket=self.channel, message=message)
    
    def close(self) -> None:
        self.ssh_client.close()
        # self.channel.close()
