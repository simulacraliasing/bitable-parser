from .query_pre_hire_response_body import QueryPreHireResponseBody as QueryPreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryPreHireResponse(BaseResponse):
    data: QueryPreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
