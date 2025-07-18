from .list_whiteboard_node_response_body import ListWhiteboardNodeResponseBody as ListWhiteboardNodeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListWhiteboardNodeResponse(BaseResponse):
    data: ListWhiteboardNodeResponseBody | None
    def __init__(self, d=None) -> None: ...
