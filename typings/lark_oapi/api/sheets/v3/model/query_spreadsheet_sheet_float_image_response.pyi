from .query_spreadsheet_sheet_float_image_response_body import QuerySpreadsheetSheetFloatImageResponseBody as QuerySpreadsheetSheetFloatImageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QuerySpreadsheetSheetFloatImageResponse(BaseResponse):
    data: QuerySpreadsheetSheetFloatImageResponseBody | None
    def __init__(self, d=None) -> None: ...
