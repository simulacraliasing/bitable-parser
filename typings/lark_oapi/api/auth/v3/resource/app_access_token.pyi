from ..model.create_app_access_token_request import CreateAppAccessTokenRequest as CreateAppAccessTokenRequest
from ..model.create_app_access_token_response import CreateAppAccessTokenResponse as CreateAppAccessTokenResponse
from ..model.internal_app_access_token_request import InternalAppAccessTokenRequest as InternalAppAccessTokenRequest
from ..model.internal_app_access_token_response import InternalAppAccessTokenResponse as InternalAppAccessTokenResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AppAccessToken:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateAppAccessTokenRequest, option: RequestOption | None = None) -> CreateAppAccessTokenResponse: ...
    async def acreate(self, request: CreateAppAccessTokenRequest, option: RequestOption | None = None) -> CreateAppAccessTokenResponse: ...
    def internal(self, request: InternalAppAccessTokenRequest, option: RequestOption | None = None) -> InternalAppAccessTokenResponse: ...
    async def ainternal(self, request: InternalAppAccessTokenRequest, option: RequestOption | None = None) -> InternalAppAccessTokenResponse: ...
