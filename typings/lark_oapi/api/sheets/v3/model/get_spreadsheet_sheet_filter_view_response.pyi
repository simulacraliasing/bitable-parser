from .get_spreadsheet_sheet_filter_view_response_body import GetSpreadsheetSheetFilterViewResponseBody as GetSpreadsheetSheetFilterViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSpreadsheetSheetFilterViewResponse(BaseResponse):
    data: GetSpreadsheetSheetFilterViewResponseBody | None
    def __init__(self, d=None) -> None: ...
