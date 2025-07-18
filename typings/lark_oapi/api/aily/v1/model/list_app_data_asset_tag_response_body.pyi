from .data_asset_tag import DataAssetTag as DataAssetTag
from lark_oapi.core.construct import init as init

class ListAppDataAssetTagResponseBody:
    items: list[DataAssetTag] | None
    page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListAppDataAssetTagResponseBodyBuilder: ...

class ListAppDataAssetTagResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[DataAssetTag]) -> ListAppDataAssetTagResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListAppDataAssetTagResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListAppDataAssetTagResponseBodyBuilder: ...
    def build(self) -> ListAppDataAssetTagResponseBody: ...
