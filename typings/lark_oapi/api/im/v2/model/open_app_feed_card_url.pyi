from lark_oapi.core.construct import init as init

class OpenAppFeedCardUrl:
    url: str | None
    android_url: str | None
    ios_url: str | None
    pc_url: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OpenAppFeedCardUrlBuilder: ...

class OpenAppFeedCardUrlBuilder:
    def __init__(self) -> None: ...
    def url(self, url: str) -> OpenAppFeedCardUrlBuilder: ...
    def android_url(self, android_url: str) -> OpenAppFeedCardUrlBuilder: ...
    def ios_url(self, ios_url: str) -> OpenAppFeedCardUrlBuilder: ...
    def pc_url(self, pc_url: str) -> OpenAppFeedCardUrlBuilder: ...
    def build(self) -> OpenAppFeedCardUrl: ...
