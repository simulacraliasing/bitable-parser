from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetProcessFormVariableDataRequest(BaseRequest):
    process_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetProcessFormVariableDataRequestBuilder: ...

class GetProcessFormVariableDataRequestBuilder:
    def __init__(self) -> None: ...
    def process_id(self, process_id: str) -> GetProcessFormVariableDataRequestBuilder: ...
    def build(self) -> GetProcessFormVariableDataRequest: ...
