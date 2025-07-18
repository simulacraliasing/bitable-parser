from lark_oapi.core.construct import init as init

class ArchiveItem:
    item_id: str | None
    item_result: str | None
    item_result_regular: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ArchiveItemBuilder: ...

class ArchiveItemBuilder:
    def __init__(self) -> None: ...
    def item_id(self, item_id: str) -> ArchiveItemBuilder: ...
    def item_result(self, item_result: str) -> ArchiveItemBuilder: ...
    def item_result_regular(self, item_result_regular: str) -> ArchiveItemBuilder: ...
    def build(self) -> ArchiveItem: ...
