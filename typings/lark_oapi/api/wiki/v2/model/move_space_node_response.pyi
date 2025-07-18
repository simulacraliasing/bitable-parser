from .move_space_node_response_body import MoveSpaceNodeResponseBody as MoveSpaceNodeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MoveSpaceNodeResponse(BaseResponse):
    data: MoveSpaceNodeResponseBody | None
    def __init__(self, d=None) -> None: ...
