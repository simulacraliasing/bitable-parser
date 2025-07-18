from .simplelist_group_response_body import SimplelistGroupResponseBody as SimplelistGroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SimplelistGroupResponse(BaseResponse):
    data: SimplelistGroupResponseBody | None
    def __init__(self, d=None) -> None: ...
