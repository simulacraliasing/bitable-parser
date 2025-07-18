from lark_oapi.core.construct import init as init

class FeedGroupItem:
    feed_id: str | None
    feed_type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FeedGroupItemBuilder: ...

class FeedGroupItemBuilder:
    def __init__(self) -> None: ...
    def feed_id(self, feed_id: str) -> FeedGroupItemBuilder: ...
    def feed_type(self, feed_type: str) -> FeedGroupItemBuilder: ...
    def build(self) -> FeedGroupItem: ...
