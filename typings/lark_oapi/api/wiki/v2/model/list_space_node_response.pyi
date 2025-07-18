from .list_space_node_response_body import ListSpaceNodeResponseBody as ListSpaceNodeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSpaceNodeResponse(BaseResponse):
    data: ListSpaceNodeResponseBody | None
    def __init__(self, d=None) -> None: ...
