from .list_external_task_request_body import ListExternalTaskRequestBody as ListExternalTaskRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListExternalTaskRequest(BaseRequest):
    page_size: int | None
    page_token: str | None
    request_body: ListExternalTaskRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListExternalTaskRequestBuilder: ...

class ListExternalTaskRequestBuilder:
    def __init__(self) -> None: ...
    def page_size(self, page_size: int) -> ListExternalTaskRequestBuilder: ...
    def page_token(self, page_token: str) -> ListExternalTaskRequestBuilder: ...
    def request_body(self, request_body: ListExternalTaskRequestBody) -> ListExternalTaskRequestBuilder: ...
    def build(self) -> ListExternalTaskRequest: ...
