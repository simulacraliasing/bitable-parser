from ..model.get_permission_public_request import GetPermissionPublicRequest as GetPermissionPublicRequest
from ..model.get_permission_public_response import GetPermissionPublicResponse as GetPermissionPublicResponse
from ..model.patch_permission_public_request import PatchPermissionPublicRequest as PatchPermissionPublicRequest
from ..model.patch_permission_public_response import PatchPermissionPublicResponse as PatchPermissionPublicResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class PermissionPublic:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetPermissionPublicRequest, option: RequestOption | None = None) -> GetPermissionPublicResponse: ...
    async def aget(self, request: GetPermissionPublicRequest, option: RequestOption | None = None) -> GetPermissionPublicResponse: ...
    def patch(self, request: PatchPermissionPublicRequest, option: RequestOption | None = None) -> PatchPermissionPublicResponse: ...
    async def apatch(self, request: PatchPermissionPublicRequest, option: RequestOption | None = None) -> PatchPermissionPublicResponse: ...
