from .get_application_role_member_response_body import GetApplicationRoleMemberResponseBody as GetApplicationRoleMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetApplicationRoleMemberResponse(BaseResponse):
    data: GetApplicationRoleMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
