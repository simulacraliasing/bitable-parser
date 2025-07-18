from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class DeleteCalendarAclRequest(BaseRequest):
    calendar_id: str | None
    acl_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> DeleteCalendarAclRequestBuilder: ...

class DeleteCalendarAclRequestBuilder:
    def __init__(self) -> None: ...
    def calendar_id(self, calendar_id: str) -> DeleteCalendarAclRequestBuilder: ...
    def acl_id(self, acl_id: str) -> DeleteCalendarAclRequestBuilder: ...
    def build(self) -> DeleteCalendarAclRequest: ...
