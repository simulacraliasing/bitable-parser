from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetWorkingHoursTypeRequest(BaseRequest):
    working_hours_type_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetWorkingHoursTypeRequestBuilder: ...

class GetWorkingHoursTypeRequestBuilder:
    def __init__(self) -> None: ...
    def working_hours_type_id(self, working_hours_type_id: str) -> GetWorkingHoursTypeRequestBuilder: ...
    def build(self) -> GetWorkingHoursTypeRequest: ...
