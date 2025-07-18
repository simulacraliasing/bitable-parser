from .find_spreadsheet_sheet_response_body import FindSpreadsheetSheetResponseBody as FindSpreadsheetSheetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class FindSpreadsheetSheetResponse(BaseResponse):
    data: FindSpreadsheetSheetResponseBody | None
    def __init__(self, d=None) -> None: ...
