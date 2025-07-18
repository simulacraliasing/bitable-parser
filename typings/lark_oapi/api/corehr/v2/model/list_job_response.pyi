from .list_job_response_body import ListJobResponseBody as ListJobResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobResponse(BaseResponse):
    data: ListJobResponseBody | None
    def __init__(self, d=None) -> None: ...
