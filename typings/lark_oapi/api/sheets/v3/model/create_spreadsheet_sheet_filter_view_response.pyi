from .create_spreadsheet_sheet_filter_view_response_body import CreateSpreadsheetSheetFilterViewResponseBody as CreateSpreadsheetSheetFilterViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSpreadsheetSheetFilterViewResponse(BaseResponse):
    data: CreateSpreadsheetSheetFilterViewResponseBody | None
    def __init__(self, d=None) -> None: ...
