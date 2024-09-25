import os
import re
import errno
import random
import configparser


def read_text(path:str):
    with open(path,"r",encoding="utf-8") as f:
        return f.read().splitlines()

def random_select(data:list):
    return random.choice(data)

def check_config(config_path:str) -> configparser.ConfigParser:

    if not os.path.exists(config_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_path)
    
    return configparser.ConfigParser()

def check_json_missing_part(responces:str) -> int:
    count = 0

    for word in responces:
        if word == "{":
            count += 1
        elif word == "}":
            count -= 1
    
    return count

def get_index_from_name(agent_name:str) -> int:
    """
    Extract numbers from the agent's string.
    Agent[01] -> 1

    Args:
        agent_name (str): Agent name string.
    
    Returns:
        int: Agent Number.
    """

    return int(re.sub('[a-zA-Z\[\]]', '',agent_name))

def index_to_agent_format(agent_index:int) -> str:
    """
    Produces a string of “Agent[?]” from the specified number.

    Args:
        agent_index (str): Agent Number.
    
    Returns:
        int: Agent name string.
    """

    return "Agent[{agent_index:0>2d}]".format(agent_index=agent_index)