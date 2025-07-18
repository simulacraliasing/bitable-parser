from .add_role_assign_authorization_response_body import AddRoleAssignAuthorizationResponseBody as AddRoleAssignAuthorizationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddRoleAssignAuthorizationResponse(BaseResponse):
    data: AddRoleAssignAuthorizationResponseBody | None
    def __init__(self, d=None) -> None: ...
