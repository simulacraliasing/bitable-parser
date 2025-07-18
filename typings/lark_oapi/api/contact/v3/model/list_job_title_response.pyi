from .list_job_title_response_body import ListJobTitleResponseBody as ListJobTitleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobTitleResponse(BaseResponse):
    data: ListJobTitleResponseBody | None
    def __init__(self, d=None) -> None: ...
