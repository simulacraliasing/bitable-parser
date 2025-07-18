from .query_session_response_body import QuerySessionResponseBody as QuerySessionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QuerySessionResponse(BaseResponse):
    data: QuerySessionResponseBody | None
    def __init__(self, d=None) -> None: ...
