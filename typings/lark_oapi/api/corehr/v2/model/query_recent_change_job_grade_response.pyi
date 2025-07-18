from .query_recent_change_job_grade_response_body import QueryRecentChangeJobGradeResponseBody as QueryRecentChangeJobGradeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRecentChangeJobGradeResponse(BaseResponse):
    data: QueryRecentChangeJobGradeResponseBody | None
    def __init__(self, d=None) -> None: ...
