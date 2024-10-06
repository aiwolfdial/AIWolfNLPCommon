from .map.status_map import StatusMap
from .map.role_map import RoleMap
from .map.remain_talk_map import RemainTalkMap
from .list.vote_list import VoteList
from .list.talk_list import TalkList
from .list.existing_role_list import ExistingRoleList
from .list.last_dead_agent_list import LastDeadAgentList


class GameInfo:
    day: int
    agent: str
    vote_list: VoteList
    latest_vote_list: VoteList
    attack_vote_list: VoteList
    latest_attack_vote_list: VoteList
    talk_list: TalkList
    whisper_list: TalkList
    status_map: StatusMap
    role_map: RoleMap
    remain_talk_map: RemainTalkMap
    remain_whisper_map: RemainTalkMap
    existing_role_list: ExistingRoleList
    last_dead_agent_list: LastDeadAgentList

    def set_received_info(self, receive_info: dict) -> None:
        if receive_info.get("gameInfo") is None:
            return

        game_info = receive_info["gameInfo"]

        self.set_day(receive_info=game_info)
        self.set_agent(receive_info=game_info)
        self.set_vote_list(receive_info=game_info)
        self.set_latest_vote_list(receive_info=game_info)
        self.set_attack_vote_list(receive_info=game_info)
        self.set_latest_attack_vote_list(receive_info=game_info)
        self.set_talk_list(receive_info=game_info)
        self.set_whisper_list(receive_info=game_info)
        self.set_status_map(receive_info=game_info)
        self.set_role_map(receive_info=game_info)
        self.set_remain_talk_map(receive_info=game_info)
        self.set_remain_whisper_map(receive_info=game_info)
        self.set_existing_role_list(receive_info=game_info)
        self.set_last_dead_agent_list(receive_info=game_info)

    def set_day(self, receive_info: dict) -> None:
        self.day = receive_info["day"]

    def set_agent(self, receive_info: dict) -> None:
        self.agent = receive_info["agent"]

    def set_vote_list(self, receive_info: dict) -> None:
        self.vote_list.set_received_info(set_list=receive_info["voteList"])

    def set_latest_vote_list(self, receive_info: dict) -> None:
        self.latest_vote_list.set_received_info(set_list=receive_info["latestVoteList"])

    def set_attack_vote_list(self, receive_info: dict) -> None:
        self.attack_vote_list.set_received_info(set_list=receive_info["attackVoteList"])

    def set_latest_attack_vote_list(self, receive_info: dict) -> None:
        self.latest_attack_vote_list.set_received_info(
            set_list=receive_info["latestAttackVoteList"]
        )

    def set_talk_list(self, receive_info: dict) -> None:
        self.talk_list.set_received_info(set_list=receive_info["talkList"])

    def set_whisper_list(self, receive_info: dict) -> None:
        self.whisper_list.set_received_info(set_list=receive_info["whisperList"])

    def set_status_map(self, receive_info: dict) -> None:
        self.status_map.set_received_info(set_map=receive_info["statusMap"])

    def set_role_map(self, receive_info: dict) -> None:
        self.role_map.set_received_info(set_map=receive_info["roleMap"])

    def set_remain_talk_map(self, receive_info: dict) -> None:
        self.remain_talk_map.set_received_info(set_map=receive_info["remainTalkMap"])

    def set_remain_whisper_map(self, receive_info: dict) -> None:
        self.remain_whisper_map.set_received_info(set_map=receive_info["remainWhisperMap"])

    def set_existing_role_list(self, receive_info: dict) -> None:
        self.existing_role_list.set_received_info(set_map=receive_info["existingRoleList"])

    def set_last_dead_agent_list(self, receive_info: dict) -> None:
        self.last_dead_agent_list.set_received_info(set_list=receive_info["lastDeadAgentList"])
