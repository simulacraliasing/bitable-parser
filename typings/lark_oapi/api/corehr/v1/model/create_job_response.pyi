from .create_job_response_body import CreateJobResponseBody as CreateJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateJobResponse(BaseResponse):
    data: CreateJobResponseBody | None
    def __init__(self, d=None) -> None: ...
