from .list_job_data_response_body import ListJobDataResponseBody as ListJobDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobDataResponse(BaseResponse):
    data: ListJobDataResponseBody | None
    def __init__(self, d=None) -> None: ...
