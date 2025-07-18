from .query_recent_change_job_response_body import QueryRecentChangeJobResponseBody as QueryRecentChangeJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeJobResponse(BaseResponse):
    data: QueryRecentChangeJobResponseBody | None
    def __init__(self, d=None) -> None: ...
