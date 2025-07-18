from .update_role_assign_authorization_response_body import UpdateRoleAssignAuthorizationResponseBody as UpdateRoleAssignAuthorizationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateRoleAssignAuthorizationResponse(BaseResponse):
    data: UpdateRoleAssignAuthorizationResponseBody | None
    def __init__(self, d=None) -> None: ...
