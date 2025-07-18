from .get_mailgroup_member_response_body import GetMailgroupMemberResponseBody as GetMailgroupMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMailgroupMemberResponse(BaseResponse):
    data: GetMailgroupMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
