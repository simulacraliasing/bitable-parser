from lark_oapi.core.construct import init as init

class ArchiveItemValue:
    item_id: str | None
    item_value: str | None
    item_value_regular: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ArchiveItemValueBuilder: ...

class ArchiveItemValueBuilder:
    def __init__(self) -> None: ...
    def item_id(self, item_id: str) -> ArchiveItemValueBuilder: ...
    def item_value(self, item_value: str) -> ArchiveItemValueBuilder: ...
    def item_value_regular(self, item_value_regular: str) -> ArchiveItemValueBuilder: ...
    def build(self) -> ArchiveItemValue: ...
