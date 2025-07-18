from .create_job_grade_response_body import CreateJobGradeResponseBody as CreateJobGradeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateJobGradeResponse(BaseResponse):
    data: CreateJobGradeResponseBody | None
    def __init__(self, d=None) -> None: ...
