from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class DeleteCategoryRequest(BaseRequest):
    id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> DeleteCategoryRequestBuilder: ...

class DeleteCategoryRequestBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> DeleteCategoryRequestBuilder: ...
    def build(self) -> DeleteCategoryRequest: ...
