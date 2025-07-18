from .get_spreadsheet_sheet_filter_response_body import GetSpreadsheetSheetFilterResponseBody as GetSpreadsheetSheetFilterResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSpreadsheetSheetFilterResponse(BaseResponse):
    data: GetSpreadsheetSheetFilterResponseBody | None
    def __init__(self, d=None) -> None: ...
