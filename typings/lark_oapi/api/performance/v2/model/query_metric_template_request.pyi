from .query_metric_template_request_body import QueryMetricTemplateRequestBody as QueryMetricTemplateRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class QueryMetricTemplateRequest(BaseRequest):
    user_id_type: str | None
    page_token: str | None
    page_size: int | None
    request_body: QueryMetricTemplateRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> QueryMetricTemplateRequestBuilder: ...

class QueryMetricTemplateRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> QueryMetricTemplateRequestBuilder: ...
    def page_token(self, page_token: str) -> QueryMetricTemplateRequestBuilder: ...
    def page_size(self, page_size: int) -> QueryMetricTemplateRequestBuilder: ...
    def request_body(self, request_body: QueryMetricTemplateRequestBody) -> QueryMetricTemplateRequestBuilder: ...
    def build(self) -> QueryMetricTemplateRequest: ...
