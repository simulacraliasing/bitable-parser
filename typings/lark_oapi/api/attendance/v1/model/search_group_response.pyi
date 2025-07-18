from .search_group_response_body import SearchGroupResponseBody as SearchGroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchGroupResponse(BaseResponse):
    data: SearchGroupResponseBody | None
    def __init__(self, d=None) -> None: ...
