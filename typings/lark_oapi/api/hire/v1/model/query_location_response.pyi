from .query_location_response_body import QueryLocationResponseBody as QueryLocationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryLocationResponse(BaseResponse):
    data: QueryLocationResponseBody | None
    def __init__(self, d=None) -> None: ...
