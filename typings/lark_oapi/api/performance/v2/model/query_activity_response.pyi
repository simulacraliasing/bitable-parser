from .query_activity_response_body import QueryActivityResponseBody as QueryActivityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryActivityResponse(BaseResponse):
    data: QueryActivityResponseBody | None
    def __init__(self, d=None) -> None: ...
