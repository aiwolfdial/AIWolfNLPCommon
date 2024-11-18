from aiwolf_nlp_common.action import Action


def check_is_action(
    target_json: dict,
    is_name: bool = False,
    is_initialize: bool = False,
    is_daily_initialize: bool = False,
    is_talk: bool = False,
    is_daily_finish: bool = False,
    is_divine: bool = False,
    is_vote: bool = False,
    is_attack: bool = False,
    is_finish: bool = False,
) -> None:
    request = target_json["request"]

    if is_name:
        assert Action.is_name(request=request)
    else:
        assert not Action.is_name(request=request)

    if is_initialize:
        assert Action.is_initialize(request=request)
    else:
        assert not Action.is_initialize(request=request)

    if is_daily_initialize:
        assert Action.is_daily_initialize(request=request)
    else:
        assert not Action.is_daily_initialize(request=request)

    if is_talk:
        assert Action.is_talk(request=request)
    else:
        assert not Action.is_talk(request=request)

    if is_daily_finish:
        assert Action.is_daily_finish(request=request)
    else:
        assert not Action.is_daily_finish(request=request)

    if is_divine:
        assert Action.is_divine(request=request)
    else:
        assert not Action.is_divine(request=request)

    if is_vote:
        assert Action.is_vote(request=request)
    else:
        assert not Action.is_vote(request=request)

    if is_attack:
        assert Action.is_attack(request=request)
    else:
        assert not Action.is_attack(request=request)

    if is_finish:
        assert Action.is_finish(request=request)
    else:
        assert not Action.is_finish(request=request)


def test_name(name_json) -> None:
    check_is_action(target_json=name_json, is_name=True)


def test_initialize(initialize_json) -> None:
    check_is_action(target_json=initialize_json, is_initialize=True)


def test_daily_initialize(daily_initialize_json) -> None:
    check_is_action(target_json=daily_initialize_json, is_daily_initialize=True)


def test_talk(talk_json) -> None:
    check_is_action(target_json=talk_json, is_talk=True)


def test_daily_finish(daily_finish_json) -> None:
    check_is_action(target_json=daily_finish_json, is_daily_finish=True)


def test_divine(divine_json) -> None:
    check_is_action(target_json=divine_json, is_divine=True)


def test_vote(vote_json) -> None:
    check_is_action(target_json=vote_json, is_vote=True)


def test_attack(attack_json) -> None:
    check_is_action(target_json=attack_json, is_attack=True)


def test_finish(finish_json) -> None:
    check_is_action(target_json=finish_json, is_finish=True)
