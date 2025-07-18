from .query_user_stats_data_response_body import QueryUserStatsDataResponseBody as QueryUserStatsDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserStatsDataResponse(BaseResponse):
    data: QueryUserStatsDataResponseBody | None
    def __init__(self, d=None) -> None: ...
