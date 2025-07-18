from .search_entity_response_body import SearchEntityResponseBody as SearchEntityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchEntityResponse(BaseResponse):
    data: SearchEntityResponseBody | None
    def __init__(self, d=None) -> None: ...
