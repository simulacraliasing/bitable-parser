from .search_enum_response_body import SearchEnumResponseBody as SearchEnumResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchEnumResponse(BaseResponse):
    data: SearchEnumResponseBody | None
    def __init__(self, d=None) -> None: ...
