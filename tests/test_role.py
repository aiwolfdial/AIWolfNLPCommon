from aiwolf_nlp_common.role import AIWolfNLPRole

def test_exist_role(role_num_map) -> None:
    for role in role_num_map.keys():
        assert AIWolfNLPRole.is_exist_role(role=role)
    
    not_exist_role = ["ABC", "Villager", "ROLE"]

    for role in not_exist_role:
        assert not AIWolfNLPRole.is_exist_role(role=role)

def test_is_villager() -> None:
    psq