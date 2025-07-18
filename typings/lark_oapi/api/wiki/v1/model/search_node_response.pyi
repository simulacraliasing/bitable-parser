from .search_node_response_body import SearchNodeResponseBody as SearchNodeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchNodeResponse(BaseResponse):
    data: SearchNodeResponseBody | None
    def __init__(self, d=None) -> None: ...
