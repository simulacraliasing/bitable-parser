from .query_user_stats_field_response_body import QueryUserStatsFieldResponseBody as QueryUserStatsFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserStatsFieldResponse(BaseResponse):
    data: QueryUserStatsFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
