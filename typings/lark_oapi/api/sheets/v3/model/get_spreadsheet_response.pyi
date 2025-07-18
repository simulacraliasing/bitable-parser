from .get_spreadsheet_response_body import GetSpreadsheetResponseBody as GetSpreadsheetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSpreadsheetResponse(BaseResponse):
    data: GetSpreadsheetResponseBody | None
    def __init__(self, d=None) -> None: ...
