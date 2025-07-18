from .get_permission_public_response_body import GetPermissionPublicResponseBody as GetPermissionPublicResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetPermissionPublicResponse(BaseResponse):
    data: GetPermissionPublicResponseBody | None
    def __init__(self, d=None) -> None: ...
