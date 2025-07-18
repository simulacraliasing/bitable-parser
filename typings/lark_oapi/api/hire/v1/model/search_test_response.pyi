from .search_test_response_body import SearchTestResponseBody as SearchTestResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchTestResponse(BaseResponse):
    data: SearchTestResponseBody | None
    def __init__(self, d=None) -> None: ...
