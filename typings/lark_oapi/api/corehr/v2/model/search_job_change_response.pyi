from .search_job_change_response_body import SearchJobChangeResponseBody as SearchJobChangeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchJobChangeResponse(BaseResponse):
    data: SearchJobChangeResponseBody | None
    def __init__(self, d=None) -> None: ...
