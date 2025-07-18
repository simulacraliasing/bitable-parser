from .simplelist_group_member_response_body import SimplelistGroupMemberResponseBody as SimplelistGroupMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SimplelistGroupMemberResponse(BaseResponse):
    data: SimplelistGroupMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
