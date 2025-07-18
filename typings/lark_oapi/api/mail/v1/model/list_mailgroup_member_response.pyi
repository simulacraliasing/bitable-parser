from .list_mailgroup_member_response_body import ListMailgroupMemberResponseBody as ListMailgroupMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMailgroupMemberResponse(BaseResponse):
    data: ListMailgroupMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
