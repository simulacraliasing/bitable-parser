from .list_scope_response_body import ListScopeResponseBody as ListScopeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListScopeResponse(BaseResponse):
    data: ListScopeResponseBody | None
    def __init__(self, d=None) -> None: ...
