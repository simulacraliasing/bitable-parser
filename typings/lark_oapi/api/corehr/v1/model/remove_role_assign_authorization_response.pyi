from .remove_role_assign_authorization_response_body import RemoveRoleAssignAuthorizationResponseBody as RemoveRoleAssignAuthorizationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RemoveRoleAssignAuthorizationResponse(BaseResponse):
    data: RemoveRoleAssignAuthorizationResponseBody | None
    def __init__(self, d=None) -> None: ...
