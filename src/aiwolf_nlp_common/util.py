"""This module provides auxiliary functions that may be used in AIWolfNLP."""

from __future__ import annotations

import configparser
import errno
import os
import random
import re
from pathlib import Path

from aiwolf_nlp_common.connection.ssh import SSHServer
from aiwolf_nlp_common.connection.tcp import TCPClient, TCPServer
from aiwolf_nlp_common.connection.websocket import WebSocketClient

ENCODE_FORMAT: str = "utf-8"


def random_select(data: list) -> object:
    """Select one element at random from the list.

    Args:
        data (str): A list of elements to be randomly selected.

    Returns:
        object: One randomly selected element.

    """
    return random.choice(data)


def is_file_exists(file_path: str) -> bool:
    """Check if the file at the specified path exists.

    Args:
        file_path (str): file path.

    Returns:
        bool: True if the file exists, False otherwise.

    """
    return Path(file_path).is_file()


def is_directory_exists(directory_path: str) -> bool:
    """Check if the directory at the specified path exists.

    Args:
        directory_path (str): directory path.

    Returns:
        bool: True if the directory_path exists, False otherwise.

    """
    return Path(directory_path).is_dir()


def read_config_file(config_file_path: str) -> configparser.ConfigParser:
    """Reads the specified config file.

    Args:
        config_file_path (str): config file path

    Returns:
        configparser.ConfigParser: ConfigParser that reads the config file.

    Raises:
        FileNotFoundError: If the file does not exist at the specified path.

    """
    if not is_file_exists(file_path=config_file_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_file_path)

    config_file = configparser.ConfigParser()
    config_file.read(config_file_path, ENCODE_FORMAT)

    return config_file


def read_text_file(text_file_path: str) -> list:
    """Read text files.

    Args:
        text_file_path (str): text file path

    Returns:
        list: Each line of a text file.

    Raises:
        FileNotFoundError: If the file does not exist at the specified path.

    """
    if not is_file_exists(file_path=text_file_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), text_file_path)

    with Path(text_file_path).open(mode="r", encoding=ENCODE_FORMAT) as f:
        return f.read().splitlines()


def get_index_from_name(agent_name: str) -> int:
    """Extract numbers from the agent's string.

    Extract the number from a string like "Agent[01]" -> 1.

    Args:
        agent_name (str): Agent name string.

    Returns:
        int: Agent Number.

    """
    return int(re.sub(r"[a-zA-Z\[\]]", "", agent_name))


def get_name_from_index(agent_index: int) -> str:
    """Produces a string of “Agent[?]” from the specified number.

    Generate the agent's name from a number, like 1 -> "Agent[01]".

    Args:
        agent_index (str): Agent Number.

    Returns:
        int: Agent name string.

    """
    return f"Agent[{agent_index:0>2d}]"


def get_socket(
    inifile: configparser.ConfigParser, name: str
) -> TCPClient | TCPServer | SSHServer | WebSocketClient:
    if inifile.getboolean("connection", "websocket"):
        return WebSocketClient(inifile=inifile)

    if inifile.getboolean("connection", "ssh"):
        return SSHServer(inifile=inifile, name=name)

    if inifile.getboolean("connection", "is_host"):
        return TCPServer(inifile=inifile, name=name)

    return TCPClient(inifile=inifile)
