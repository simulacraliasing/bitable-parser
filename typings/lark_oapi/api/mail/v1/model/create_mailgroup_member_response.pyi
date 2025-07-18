from .create_mailgroup_member_response_body import CreateMailgroupMemberResponseBody as CreateMailgroupMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateMailgroupMemberResponse(BaseResponse):
    data: CreateMailgroupMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
