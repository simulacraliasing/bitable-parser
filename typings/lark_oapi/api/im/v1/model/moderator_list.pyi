from .list_event_moderator import ListEventModerator as ListEventModerator
from lark_oapi.core.construct import init as init

class ModeratorList:
    added_member_list: list[ListEventModerator] | None
    removed_member_list: list[ListEventModerator] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ModeratorListBuilder: ...

class ModeratorListBuilder:
    def __init__(self) -> None: ...
    def added_member_list(self, added_member_list: list[ListEventModerator]) -> ModeratorListBuilder: ...
    def removed_member_list(self, removed_member_list: list[ListEventModerator]) -> ModeratorListBuilder: ...
    def build(self) -> ModeratorList: ...
