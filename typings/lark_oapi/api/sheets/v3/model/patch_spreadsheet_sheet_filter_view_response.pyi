from .patch_spreadsheet_sheet_filter_view_response_body import PatchSpreadsheetSheetFilterViewResponseBody as PatchSpreadsheetSheetFilterViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchSpreadsheetSheetFilterViewResponse(BaseResponse):
    data: PatchSpreadsheetSheetFilterViewResponseBody | None
    def __init__(self, d=None) -> None: ...
