from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListMetricTagRequest(BaseRequest):
    page_size: int | None
    page_token: str | None
    tag_ids: list[str] | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListMetricTagRequestBuilder: ...

class ListMetricTagRequestBuilder:
    def __init__(self) -> None: ...
    def page_size(self, page_size: int) -> ListMetricTagRequestBuilder: ...
    def page_token(self, page_token: str) -> ListMetricTagRequestBuilder: ...
    def tag_ids(self, tag_ids: list[str]) -> ListMetricTagRequestBuilder: ...
    def build(self) -> ListMetricTagRequest: ...
