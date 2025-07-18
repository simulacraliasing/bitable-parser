from .list_file_response_body import ListFileResponseBody as ListFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFileResponse(BaseResponse):
    data: ListFileResponseBody | None
    def __init__(self, d=None) -> None: ...
