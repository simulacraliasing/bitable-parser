from .get_job_manager_response_body import GetJobManagerResponseBody as GetJobManagerResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetJobManagerResponse(BaseResponse):
    data: GetJobManagerResponseBody | None
    def __init__(self, d=None) -> None: ...
