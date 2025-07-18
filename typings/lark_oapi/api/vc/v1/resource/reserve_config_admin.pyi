from ..model.get_reserve_config_admin_request import GetReserveConfigAdminRequest as GetReserveConfigAdminRequest
from ..model.get_reserve_config_admin_response import GetReserveConfigAdminResponse as GetReserveConfigAdminResponse
from ..model.patch_reserve_config_admin_request import PatchReserveConfigAdminRequest as PatchReserveConfigAdminRequest
from ..model.patch_reserve_config_admin_response import PatchReserveConfigAdminResponse as PatchReserveConfigAdminResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ReserveConfigAdmin:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetReserveConfigAdminRequest, option: RequestOption | None = None) -> GetReserveConfigAdminResponse: ...
    async def aget(self, request: GetReserveConfigAdminRequest, option: RequestOption | None = None) -> GetReserveConfigAdminResponse: ...
    def patch(self, request: PatchReserveConfigAdminRequest, option: RequestOption | None = None) -> PatchReserveConfigAdminResponse: ...
    async def apatch(self, request: PatchReserveConfigAdminRequest, option: RequestOption | None = None) -> PatchReserveConfigAdminResponse: ...
