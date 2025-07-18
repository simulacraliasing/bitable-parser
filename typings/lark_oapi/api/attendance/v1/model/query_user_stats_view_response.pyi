from .query_user_stats_view_response_body import QueryUserStatsViewResponseBody as QueryUserStatsViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserStatsViewResponse(BaseResponse):
    data: QueryUserStatsViewResponseBody | None
    def __init__(self, d=None) -> None: ...
