from .patch_spreadsheet_sheet_float_image_response_body import PatchSpreadsheetSheetFloatImageResponseBody as PatchSpreadsheetSheetFloatImageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchSpreadsheetSheetFloatImageResponse(BaseResponse):
    data: PatchSpreadsheetSheetFloatImageResponseBody | None
    def __init__(self, d=None) -> None: ...
