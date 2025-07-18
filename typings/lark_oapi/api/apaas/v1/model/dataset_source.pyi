from .dataset_source_setting import DatasetSourceSetting as DatasetSourceSetting
from lark_oapi.core.construct import init as init

class DatasetSource:
    type: str | None
    settings: DatasetSourceSetting | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DatasetSourceBuilder: ...

class DatasetSourceBuilder:
    def __init__(self) -> None: ...
    def type(self, type: str) -> DatasetSourceBuilder: ...
    def settings(self, settings: DatasetSourceSetting) -> DatasetSourceBuilder: ...
    def build(self) -> DatasetSource: ...
