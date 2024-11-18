import aiwolf_nlp_common.util as util


def test_is_file_exist(text_file_path: str, config_file_path: str) -> None:
    assert util.is_file_exists(file_path=text_file_path)
    assert util.is_file_exists(file_path=config_file_path)

    assert not util.is_file_exists(file_path=text_file_path + ".test")
    assert not util.is_file_exists(file_path=config_file_path.replace("/", ""))


def test_is_directory_exists() -> None:
    dir_path = "tests/AIWolfNLAgentPython/res/"
    assert util.is_directory_exists(directory_path=dir_path)

    dir_path = "tests/AIWolfNLAgentPython/res"
    assert util.is_directory_exists(directory_path=dir_path)

    dir_path = "tests/AIWolfNLAgentPython/res/test"
    assert not util.is_directory_exists(directory_path=dir_path)

    dir_path = "tests/AIWolfNLAgentPython/re"
    assert not util.is_directory_exists(directory_path=dir_path)


def test_read_config_file(text_file_path: str, config_file_path: str) -> None:
    config_file = util.read_config_file(config_file_path=config_file_path)
    assert config_file.get("agent", "name1") == "kanolab1"

    config_file = util.read_config_file(config_file_path=config_file_path)
    assert config_file.get("filePath", "random_talk") == text_file_path

    config_file = util.read_config_file(config_file_path=config_file_path)
    assert not config_file.get("agent", "name1") == "kanolab2"

    config_file = util.read_config_file(config_file_path=config_file_path)
    assert not config_file.get("filePath", "random_talk") == config_file_path


def test_read_text_file(text_file_path: str) -> None:
    with open(text_file_path, "r", encoding="utf-8") as f:
        correct_list = f.read().splitlines()

    check_list = util.read_text_file(text_file_path=text_file_path)

    correct_list.sort()
    check_list.sort()

    assert correct_list == check_list


def test_get_index_and_name() -> None:
    for i in range(20):
        if i < 10:
            name = "Agent[0" + str(i) + "]"
        else:
            name = "Agent[" + str(i) + "]"

        assert i == util.get_index_from_name(agent_name=name)
        assert name == util.get_name_from_index(agent_index=i)
