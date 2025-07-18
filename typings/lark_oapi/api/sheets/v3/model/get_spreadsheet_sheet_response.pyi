from .get_spreadsheet_sheet_response_body import GetSpreadsheetSheetResponseBody as GetSpreadsheetSheetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSpreadsheetSheetResponse(BaseResponse):
    data: GetSpreadsheetSheetResponseBody | None
    def __init__(self, d=None) -> None: ...
