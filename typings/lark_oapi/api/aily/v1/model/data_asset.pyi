from .data_asset_import_knowledge_setting import DataAssetImportKnowledgeSetting as DataAssetImportKnowledgeSetting
from .data_asset_item import DataAssetItem as DataAssetItem
from .data_asset_tag import DataAssetTag as DataAssetTag
from lark_oapi.core.construct import init as init

class DataAsset:
    data_asset_id: str | None
    label: dict[str, str] | None
    description: dict[str, str] | None
    data_source_type: str | None
    connect_status: str | None
    tags: list[DataAssetTag] | None
    items: list[DataAssetItem] | None
    connect_failed_reason: str | None
    import_knowledge_setting: DataAssetImportKnowledgeSetting | None
    connect_type: str | None
    created_time: int | None
    updated_time: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DataAssetBuilder: ...

class DataAssetBuilder:
    def __init__(self) -> None: ...
    def data_asset_id(self, data_asset_id: str) -> DataAssetBuilder: ...
    def label(self, label: dict[str, str]) -> DataAssetBuilder: ...
    def description(self, description: dict[str, str]) -> DataAssetBuilder: ...
    def data_source_type(self, data_source_type: str) -> DataAssetBuilder: ...
    def connect_status(self, connect_status: str) -> DataAssetBuilder: ...
    def tags(self, tags: list[DataAssetTag]) -> DataAssetBuilder: ...
    def items(self, items: list[DataAssetItem]) -> DataAssetBuilder: ...
    def connect_failed_reason(self, connect_failed_reason: str) -> DataAssetBuilder: ...
    def import_knowledge_setting(self, import_knowledge_setting: DataAssetImportKnowledgeSetting) -> DataAssetBuilder: ...
    def connect_type(self, connect_type: str) -> DataAssetBuilder: ...
    def created_time(self, created_time: int) -> DataAssetBuilder: ...
    def updated_time(self, updated_time: int) -> DataAssetBuilder: ...
    def build(self) -> DataAsset: ...
