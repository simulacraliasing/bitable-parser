from .query_job_grade_response_body import QueryJobGradeResponseBody as QueryJobGradeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryJobGradeResponse(BaseResponse):
    data: QueryJobGradeResponseBody | None
    def __init__(self, d=None) -> None: ...
