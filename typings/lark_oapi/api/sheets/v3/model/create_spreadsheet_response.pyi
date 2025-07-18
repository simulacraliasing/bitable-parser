from .create_spreadsheet_response_body import CreateSpreadsheetResponseBody as CreateSpreadsheetResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSpreadsheetResponse(BaseResponse):
    data: CreateSpreadsheetResponseBody | None
    def __init__(self, d=None) -> None: ...
