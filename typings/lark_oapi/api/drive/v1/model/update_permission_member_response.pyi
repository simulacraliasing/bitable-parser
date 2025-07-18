from .update_permission_member_response_body import UpdatePermissionMemberResponseBody as UpdatePermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdatePermissionMemberResponse(BaseResponse):
    data: UpdatePermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
