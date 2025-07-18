from .get_node_space_response_body import GetNodeSpaceResponseBody as GetNodeSpaceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetNodeSpaceResponse(BaseResponse):
    data: GetNodeSpaceResponseBody | None
    def __init__(self, d=None) -> None: ...
