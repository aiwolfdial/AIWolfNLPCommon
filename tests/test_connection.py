from aiwolf_nlp_common.client import Client


def test_split_receive_info() -> None:
    log_name_json: str = """{"request": "NAME"}"""
    multi_json: str = (
        """{"request": "NAME"}\n{"request": "NAME"}\n{"request": "NAME"}\n{"request": "NAME"}\n{"request": "NAME"}\n"""
    )

    correct_list: list = [log_name_json] * 5

    assert Client.split_receives(receive=multi_json) == correct_list

    multi_json: str = """{"request": "NAME"}\n"""
    assert Client.split_receives(receive=multi_json) == [log_name_json]
