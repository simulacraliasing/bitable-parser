from .filter_view import FilterView as FilterView
from lark_oapi.core.construct import init as init

class GetSpreadsheetSheetFilterViewResponseBody:
    filter_view: FilterView | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetSpreadsheetSheetFilterViewResponseBodyBuilder: ...

class GetSpreadsheetSheetFilterViewResponseBodyBuilder:
    def __init__(self) -> None: ...
    def filter_view(self, filter_view: FilterView) -> GetSpreadsheetSheetFilterViewResponseBodyBuilder: ...
    def build(self) -> GetSpreadsheetSheetFilterViewResponseBody: ...
