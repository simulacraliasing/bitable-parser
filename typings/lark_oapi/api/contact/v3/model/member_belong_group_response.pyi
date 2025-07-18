from .member_belong_group_response_body import MemberBelongGroupResponseBody as MemberBelongGroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MemberBelongGroupResponse(BaseResponse):
    data: MemberBelongGroupResponseBody | None
    def __init__(self, d=None) -> None: ...
