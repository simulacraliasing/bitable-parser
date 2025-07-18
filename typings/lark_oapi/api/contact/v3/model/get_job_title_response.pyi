from .get_job_title_response_body import GetJobTitleResponseBody as GetJobTitleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetJobTitleResponse(BaseResponse):
    data: GetJobTitleResponseBody | None
    def __init__(self, d=None) -> None: ...
