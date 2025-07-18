from .update_spreadsheet_properties import UpdateSpreadsheetProperties as UpdateSpreadsheetProperties
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchSpreadsheetRequest(BaseRequest):
    spreadsheet_token: str | None
    request_body: UpdateSpreadsheetProperties | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchSpreadsheetRequestBuilder: ...

class PatchSpreadsheetRequestBuilder:
    def __init__(self) -> None: ...
    def spreadsheet_token(self, spreadsheet_token: str) -> PatchSpreadsheetRequestBuilder: ...
    def request_body(self, request_body: UpdateSpreadsheetProperties) -> PatchSpreadsheetRequestBuilder: ...
    def build(self) -> PatchSpreadsheetRequest: ...
