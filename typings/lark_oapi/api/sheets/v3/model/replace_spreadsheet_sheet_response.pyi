from .replace_spreadsheet_sheet_response_body import ReplaceSpreadsheetSheetResponseBody as ReplaceSpreadsheetSheetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ReplaceSpreadsheetSheetResponse(BaseResponse):
    data: ReplaceSpreadsheetSheetResponseBody | None
    def __init__(self, d=None) -> None: ...
