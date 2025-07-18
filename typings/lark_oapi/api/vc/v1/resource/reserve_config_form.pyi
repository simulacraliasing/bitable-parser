from ..model.get_reserve_config_form_request import GetReserveConfigFormRequest as GetReserveConfigFormRequest
from ..model.get_reserve_config_form_response import GetReserveConfigFormResponse as GetReserveConfigFormResponse
from ..model.patch_reserve_config_form_request import PatchReserveConfigFormRequest as PatchReserveConfigFormRequest
from ..model.patch_reserve_config_form_response import PatchReserveConfigFormResponse as PatchReserveConfigFormResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ReserveConfigForm:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetReserveConfigFormRequest, option: RequestOption | None = None) -> GetReserveConfigFormResponse: ...
    async def aget(self, request: GetReserveConfigFormRequest, option: RequestOption | None = None) -> GetReserveConfigFormResponse: ...
    def patch(self, request: PatchReserveConfigFormRequest, option: RequestOption | None = None) -> PatchReserveConfigFormResponse: ...
    async def apatch(self, request: PatchReserveConfigFormRequest, option: RequestOption | None = None) -> PatchReserveConfigFormResponse: ...
