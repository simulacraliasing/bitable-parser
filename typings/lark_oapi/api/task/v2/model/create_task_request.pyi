from .input_task import InputTask as InputTask
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateTaskRequest(BaseRequest):
    user_id_type: str | None
    request_body: InputTask | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateTaskRequestBuilder: ...

class CreateTaskRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> CreateTaskRequestBuilder: ...
    def request_body(self, request_body: InputTask) -> CreateTaskRequestBuilder: ...
    def build(self) -> CreateTaskRequest: ...
