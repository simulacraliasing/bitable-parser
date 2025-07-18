from .query_spreadsheet_sheet_filter_view_response_body import QuerySpreadsheetSheetFilterViewResponseBody as QuerySpreadsheetSheetFilterViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QuerySpreadsheetSheetFilterViewResponse(BaseResponse):
    data: QuerySpreadsheetSheetFilterViewResponseBody | None
    def __init__(self, d=None) -> None: ...
