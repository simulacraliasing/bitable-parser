from .query_indicator_response_body import QueryIndicatorResponseBody as QueryIndicatorResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryIndicatorResponse(BaseResponse):
    data: QueryIndicatorResponseBody | None
    def __init__(self, d=None) -> None: ...
