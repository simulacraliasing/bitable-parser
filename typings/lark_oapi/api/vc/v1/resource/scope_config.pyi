from ..model.create_scope_config_request import CreateScopeConfigRequest as CreateScopeConfigRequest
from ..model.create_scope_config_response import CreateScopeConfigResponse as CreateScopeConfigResponse
from ..model.get_scope_config_request import GetScopeConfigRequest as GetScopeConfigRequest
from ..model.get_scope_config_response import GetScopeConfigResponse as GetScopeConfigResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ScopeConfig:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateScopeConfigRequest, option: RequestOption | None = None) -> CreateScopeConfigResponse: ...
    async def acreate(self, request: CreateScopeConfigRequest, option: RequestOption | None = None) -> CreateScopeConfigResponse: ...
    def get(self, request: GetScopeConfigRequest, option: RequestOption | None = None) -> GetScopeConfigResponse: ...
    async def aget(self, request: GetScopeConfigRequest, option: RequestOption | None = None) -> GetScopeConfigResponse: ...
