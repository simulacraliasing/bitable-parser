from .update_permission_public_password_response_body import UpdatePermissionPublicPasswordResponseBody as UpdatePermissionPublicPasswordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdatePermissionPublicPasswordResponse(BaseResponse):
    data: UpdatePermissionPublicPasswordResponseBody | None
    def __init__(self, d=None) -> None: ...
