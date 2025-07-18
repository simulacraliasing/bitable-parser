from .get_detail_job_response_body import GetDetailJobResponseBody as GetDetailJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDetailJobResponse(BaseResponse):
    data: GetDetailJobResponseBody | None
    def __init__(self, d=None) -> None: ...
