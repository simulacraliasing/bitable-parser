from ..model.update_space_setting_request import UpdateSpaceSettingRequest as UpdateSpaceSettingRequest
from ..model.update_space_setting_response import UpdateSpaceSettingResponse as UpdateSpaceSettingResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class SpaceSetting:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def update(self, request: UpdateSpaceSettingRequest, option: RequestOption | None = None) -> UpdateSpaceSettingResponse: ...
    async def aupdate(self, request: UpdateSpaceSettingRequest, option: RequestOption | None = None) -> UpdateSpaceSettingResponse: ...
