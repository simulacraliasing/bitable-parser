from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetTaskRequest(BaseRequest):
    task_type: str | None
    task_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetTaskRequestBuilder: ...

class GetTaskRequestBuilder:
    def __init__(self) -> None: ...
    def task_type(self, task_type: str) -> GetTaskRequestBuilder: ...
    def task_id(self, task_id: str) -> GetTaskRequestBuilder: ...
    def build(self) -> GetTaskRequest: ...
