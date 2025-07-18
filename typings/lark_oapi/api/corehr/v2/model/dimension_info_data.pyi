from .dimension_info import DimensionInfo as DimensionInfo
from lark_oapi.core.construct import init as init

class DimensionInfoData:
    dimension_key: str | None
    dimension_info: DimensionInfo | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DimensionInfoDataBuilder: ...

class DimensionInfoDataBuilder:
    def __init__(self) -> None: ...
    def dimension_key(self, dimension_key: str) -> DimensionInfoDataBuilder: ...
    def dimension_info(self, dimension_info: DimensionInfo) -> DimensionInfoDataBuilder: ...
    def build(self) -> DimensionInfoData: ...
