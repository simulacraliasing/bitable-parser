from .create_mailgroup_permission_member_response_body import CreateMailgroupPermissionMemberResponseBody as CreateMailgroupPermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateMailgroupPermissionMemberResponse(BaseResponse):
    data: CreateMailgroupPermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
