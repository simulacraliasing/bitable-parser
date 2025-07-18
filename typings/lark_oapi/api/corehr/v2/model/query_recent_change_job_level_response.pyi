from .query_recent_change_job_level_response_body import QueryRecentChangeJobLevelResponseBody as QueryRecentChangeJobLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeJobLevelResponse(BaseResponse):
    data: QueryRecentChangeJobLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
