from .patch_permission_public_response_body import PatchPermissionPublicResponseBody as PatchPermissionPublicResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchPermissionPublicResponse(BaseResponse):
    data: PatchPermissionPublicResponseBody | None
    def __init__(self, d=None) -> None: ...
