from .combined_create_job_response_body import CombinedCreateJobResponseBody as CombinedCreateJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CombinedCreateJobResponse(BaseResponse):
    data: CombinedCreateJobResponseBody | None
    def __init__(self, d=None) -> None: ...
