from .query_instance_response_body import QueryInstanceResponseBody as QueryInstanceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryInstanceResponse(BaseResponse):
    data: QueryInstanceResponseBody | None
    def __init__(self, d=None) -> None: ...
