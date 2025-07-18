from .create_spreadsheet_sheet_float_image_response_body import CreateSpreadsheetSheetFloatImageResponseBody as CreateSpreadsheetSheetFloatImageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSpreadsheetSheetFloatImageResponse(BaseResponse):
    data: CreateSpreadsheetSheetFloatImageResponseBody | None
    def __init__(self, d=None) -> None: ...
