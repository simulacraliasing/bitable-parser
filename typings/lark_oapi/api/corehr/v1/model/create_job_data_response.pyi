from .create_job_data_response_body import CreateJobDataResponseBody as CreateJobDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateJobDataResponse(BaseResponse):
    data: CreateJobDataResponseBody | None
    def __init__(self, d=None) -> None: ...
