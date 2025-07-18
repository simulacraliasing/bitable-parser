from ..model.patch_reserve_config_request import PatchReserveConfigRequest as PatchReserveConfigRequest
from ..model.patch_reserve_config_response import PatchReserveConfigResponse as PatchReserveConfigResponse
from ..model.reserve_scope_reserve_config_request import ReserveScopeReserveConfigRequest as ReserveScopeReserveConfigRequest
from ..model.reserve_scope_reserve_config_response import ReserveScopeReserveConfigResponse as ReserveScopeReserveConfigResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ReserveConfig:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def patch(self, request: PatchReserveConfigRequest, option: RequestOption | None = None) -> PatchReserveConfigResponse: ...
    async def apatch(self, request: PatchReserveConfigRequest, option: RequestOption | None = None) -> PatchReserveConfigResponse: ...
    def reserve_scope(self, request: ReserveScopeReserveConfigRequest, option: RequestOption | None = None) -> ReserveScopeReserveConfigResponse: ...
    async def areserve_scope(self, request: ReserveScopeReserveConfigRequest, option: RequestOption | None = None) -> ReserveScopeReserveConfigResponse: ...
