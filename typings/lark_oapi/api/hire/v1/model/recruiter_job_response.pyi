from .recruiter_job_response_body import RecruiterJobResponseBody as RecruiterJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecruiterJobResponse(BaseResponse):
    data: RecruiterJobResponseBody | None
    def __init__(self, d=None) -> None: ...
