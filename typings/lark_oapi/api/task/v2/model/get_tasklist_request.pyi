from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetTasklistRequest(BaseRequest):
    user_id_type: str | None
    tasklist_guid: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetTasklistRequestBuilder: ...

class GetTasklistRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> GetTasklistRequestBuilder: ...
    def tasklist_guid(self, tasklist_guid: str) -> GetTasklistRequestBuilder: ...
    def build(self) -> GetTasklistRequest: ...
