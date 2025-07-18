from .create_job_change_response_body import CreateJobChangeResponseBody as CreateJobChangeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateJobChangeResponse(BaseResponse):
    data: CreateJobChangeResponseBody | None
    def __init__(self, d=None) -> None: ...
