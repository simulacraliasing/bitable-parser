from ..model.get_reserve_config_disable_inform_request import GetReserveConfigDisableInformRequest as GetReserveConfigDisableInformRequest
from ..model.get_reserve_config_disable_inform_response import GetReserveConfigDisableInformResponse as GetReserveConfigDisableInformResponse
from ..model.patch_reserve_config_disable_inform_request import PatchReserveConfigDisableInformRequest as PatchReserveConfigDisableInformRequest
from ..model.patch_reserve_config_disable_inform_response import PatchReserveConfigDisableInformResponse as PatchReserveConfigDisableInformResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ReserveConfigDisableInform:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetReserveConfigDisableInformRequest, option: RequestOption | None = None) -> GetReserveConfigDisableInformResponse: ...
    async def aget(self, request: GetReserveConfigDisableInformRequest, option: RequestOption | None = None) -> GetReserveConfigDisableInformResponse: ...
    def patch(self, request: PatchReserveConfigDisableInformRequest, option: RequestOption | None = None) -> PatchReserveConfigDisableInformResponse: ...
    async def apatch(self, request: PatchReserveConfigDisableInformRequest, option: RequestOption | None = None) -> PatchReserveConfigDisableInformResponse: ...
