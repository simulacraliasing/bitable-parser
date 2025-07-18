from .openapi_log import OpenapiLog as OpenapiLog
from lark_oapi.core.construct import init as init

class ListDataOpenapiLogResponseBody:
    items: list[OpenapiLog] | None
    page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListDataOpenapiLogResponseBodyBuilder: ...

class ListDataOpenapiLogResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[OpenapiLog]) -> ListDataOpenapiLogResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListDataOpenapiLogResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListDataOpenapiLogResponseBodyBuilder: ...
    def build(self) -> ListDataOpenapiLogResponseBody: ...
