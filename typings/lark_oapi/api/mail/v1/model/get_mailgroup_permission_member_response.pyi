from .get_mailgroup_permission_member_response_body import GetMailgroupPermissionMemberResponseBody as GetMailgroupPermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMailgroupPermissionMemberResponse(BaseResponse):
    data: GetMailgroupPermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
