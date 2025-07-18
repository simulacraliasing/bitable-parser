from .get_spreadsheet_sheet_float_image_response_body import GetSpreadsheetSheetFloatImageResponseBody as GetSpreadsheetSheetFloatImageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSpreadsheetSheetFloatImageResponse(BaseResponse):
    data: GetSpreadsheetSheetFloatImageResponseBody | None
    def __init__(self, d=None) -> None: ...
