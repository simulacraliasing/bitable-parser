from .get_job_response_body import GetJobResponseBody as GetJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetJobResponse(BaseResponse):
    data: GetJobResponseBody | None
    def __init__(self, d=None) -> None: ...
