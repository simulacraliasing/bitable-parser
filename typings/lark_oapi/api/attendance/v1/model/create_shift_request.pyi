from .shift import Shift as Shift
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateShiftRequest(BaseRequest):
    employee_type: str | None
    request_body: Shift | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateShiftRequestBuilder: ...

class CreateShiftRequestBuilder:
    def __init__(self) -> None: ...
    def employee_type(self, employee_type: str) -> CreateShiftRequestBuilder: ...
    def request_body(self, request_body: Shift) -> CreateShiftRequestBuilder: ...
    def build(self) -> CreateShiftRequest: ...
