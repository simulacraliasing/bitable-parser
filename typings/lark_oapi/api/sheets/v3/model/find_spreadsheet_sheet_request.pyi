from .find import Find as Find
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class FindSpreadsheetSheetRequest(BaseRequest):
    spreadsheet_token: str | None
    sheet_id: str | None
    request_body: Find | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> FindSpreadsheetSheetRequestBuilder: ...

class FindSpreadsheetSheetRequestBuilder:
    def __init__(self) -> None: ...
    def spreadsheet_token(self, spreadsheet_token: str) -> FindSpreadsheetSheetRequestBuilder: ...
    def sheet_id(self, sheet_id: str) -> FindSpreadsheetSheetRequestBuilder: ...
    def request_body(self, request_body: Find) -> FindSpreadsheetSheetRequestBuilder: ...
    def build(self) -> FindSpreadsheetSheetRequest: ...
