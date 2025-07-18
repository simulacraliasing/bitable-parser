from .create_permission_public_password_response_body import CreatePermissionPublicPasswordResponseBody as CreatePermissionPublicPasswordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreatePermissionPublicPasswordResponse(BaseResponse):
    data: CreatePermissionPublicPasswordResponseBody | None
    def __init__(self, d=None) -> None: ...
