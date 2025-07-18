from .copy_space_node_response_body import CopySpaceNodeResponseBody as CopySpaceNodeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CopySpaceNodeResponse(BaseResponse):
    data: CopySpaceNodeResponseBody | None
    def __init__(self, d=None) -> None: ...
