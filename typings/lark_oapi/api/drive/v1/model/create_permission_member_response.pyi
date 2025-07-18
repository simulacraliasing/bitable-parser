from .create_permission_member_response_body import CreatePermissionMemberResponseBody as CreatePermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreatePermissionMemberResponse(BaseResponse):
    data: CreatePermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
