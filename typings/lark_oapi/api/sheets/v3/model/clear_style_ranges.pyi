from lark_oapi.core.construct import init as init

class ClearStyleRanges:
    ranges: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ClearStyleRangesBuilder: ...

class ClearStyleRangesBuilder:
    def __init__(self) -> None: ...
    def ranges(self, ranges: list[str]) -> ClearStyleRangesBuilder: ...
    def build(self) -> ClearStyleRanges: ...
