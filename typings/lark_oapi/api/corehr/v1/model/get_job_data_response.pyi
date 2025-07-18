from .get_job_data_response_body import GetJobDataResponseBody as GetJobDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetJobDataResponse(BaseResponse):
    data: GetJobDataResponseBody | None
    def __init__(self, d=None) -> None: ...
