from .filter_view import FilterView as FilterView
from lark_oapi.core.construct import init as init

class QuerySpreadsheetSheetFilterViewResponseBody:
    items: list[FilterView] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QuerySpreadsheetSheetFilterViewResponseBodyBuilder: ...

class QuerySpreadsheetSheetFilterViewResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[FilterView]) -> QuerySpreadsheetSheetFilterViewResponseBodyBuilder: ...
    def build(self) -> QuerySpreadsheetSheetFilterViewResponseBody: ...
