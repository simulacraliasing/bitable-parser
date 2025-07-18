from .auth_permission_member_response_body import AuthPermissionMemberResponseBody as AuthPermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AuthPermissionMemberResponse(BaseResponse):
    data: AuthPermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
