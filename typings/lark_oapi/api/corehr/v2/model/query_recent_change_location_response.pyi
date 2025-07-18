from .query_recent_change_location_response_body import QueryRecentChangeLocationResponseBody as QueryRecentChangeLocationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeLocationResponse(BaseResponse):
    data: QueryRecentChangeLocationResponseBody | None
    def __init__(self, d=None) -> None: ...
