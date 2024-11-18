from aiwolf_nlp_common.protocol.gameInfo.map.status_map import AgentStatus, Status, StatusMap


def test_set_received_info(initialize_json: dict, status_map_json: dict) -> None:
    test_map = StatusMap.initialize_from_json(set_map=initialize_json["gameInfo"]["statusMap"])

    check_set: set[AgentStatus] = set()
    for i in range(5):
        name = "Agent[0" + str(i + 1) + "]"
        add_elem = AgentStatus(agent=name, status="ALIVE")
        check_set.add(add_elem)

    assert test_map == check_set

    test_map = StatusMap.initialize_from_json(set_map=status_map_json["gameInfo"]["statusMap"])
    check_set.clear()

    for i in range(5):
        name = "Agent[0" + str(i + 1) + "]"

        if i + 1 != 1 and i + 1 != 2 and i + 1 != 3:
            check_set.add(AgentStatus(agent=name, status="ALIVE"))
        else:
            check_set.add(AgentStatus(agent=name, status="DEAD"))

    assert test_map == check_set


def test_set_alive() -> None:
    test_map = StatusMap()

    check_set: set[AgentStatus] = set()
    for i in range(5):
        name = "Agent[0" + str(i + 1) + "]"

        test_map.set_alive(agent=name)
        add_elem = AgentStatus(agent=name, status="ALIVE")
        check_set.add(add_elem)

    assert test_map == check_set


def test_set_dead() -> None:
    test_map = StatusMap()

    check_set: set[AgentStatus] = set()

    for i in range(5):
        name = "Agent[0" + str(i + 1) + "]"

        if i + 1 != 1 and i + 1 != 2 and i + 1 != 3:
            check_set.add(AgentStatus(agent=name, status="ALIVE"))
            test_map.set_alive(agent=name)
        else:
            check_set.add(AgentStatus(agent=name, status="DEAD"))
            test_map.set_dead(agent=name)

    assert test_map == check_set


def test_set_reverse_status() -> None:
    test_map = StatusMap()

    check_set: set[AgentStatus] = set()

    for i in range(5):
        name = "Agent[0" + str(i + 1) + "]"

        if i + 1 != 1 and i + 1 != 2 and i + 1 != 3:
            check_set.add(AgentStatus(agent=name, status="ALIVE"))
            test_map.set_dead(agent=name)
        else:
            check_set.add(AgentStatus(agent=name, status="DEAD"))
            test_map.set_alive(agent=name)

        test_map.reverse_status(agent=name)

    assert test_map == check_set


def test_get_agent_list(status_map_json: dict) -> None:
    test_map = StatusMap.initialize_from_json(set_map=status_map_json["gameInfo"]["statusMap"])

    alive_list = ["Agent[04]", "Agent[05]"]
    dead_list = ["Agent[01]", "Agent[02]", "Agent[03]"]

    assert test_map.get_alive_agent_list() == alive_list
    assert test_map.get_dead_agent_list() == dead_list
