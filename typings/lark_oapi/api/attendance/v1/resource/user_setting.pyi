from ..model.modify_user_setting_request import ModifyUserSettingRequest as ModifyUserSettingRequest
from ..model.modify_user_setting_response import ModifyUserSettingResponse as ModifyUserSettingResponse
from ..model.query_user_setting_request import QueryUserSettingRequest as QueryUserSettingRequest
from ..model.query_user_setting_response import QueryUserSettingResponse as QueryUserSettingResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserSetting:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def modify(self, request: ModifyUserSettingRequest, option: RequestOption | None = None) -> ModifyUserSettingResponse: ...
    async def amodify(self, request: ModifyUserSettingRequest, option: RequestOption | None = None) -> ModifyUserSettingResponse: ...
    def query(self, request: QueryUserSettingRequest, option: RequestOption | None = None) -> QueryUserSettingResponse: ...
    async def aquery(self, request: QueryUserSettingRequest, option: RequestOption | None = None) -> QueryUserSettingResponse: ...
