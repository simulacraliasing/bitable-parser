from .query_spreadsheet_sheet_response_body import QuerySpreadsheetSheetResponseBody as QuerySpreadsheetSheetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QuerySpreadsheetSheetResponse(BaseResponse):
    data: QuerySpreadsheetSheetResponseBody | None
    def __init__(self, d=None) -> None: ...
