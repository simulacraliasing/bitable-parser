from lark_oapi.core.construct import init as init

class ChatAnnouncement:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ChatAnnouncementBuilder: ...

class ChatAnnouncementBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ChatAnnouncement: ...
