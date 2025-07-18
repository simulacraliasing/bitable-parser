from .list_job_process_response_body import ListJobProcessResponseBody as ListJobProcessResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobProcessResponse(BaseResponse):
    data: ListJobProcessResponseBody | None
    def __init__(self, d=None) -> None: ...
