from ..model.create_tenant_access_token_request import CreateTenantAccessTokenRequest as CreateTenantAccessTokenRequest
from ..model.create_tenant_access_token_response import CreateTenantAccessTokenResponse as CreateTenantAccessTokenResponse
from ..model.internal_tenant_access_token_request import InternalTenantAccessTokenRequest as InternalTenantAccessTokenRequest
from ..model.internal_tenant_access_token_response import InternalTenantAccessTokenResponse as InternalTenantAccessTokenResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TenantAccessToken:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTenantAccessTokenRequest, option: RequestOption | None = None) -> CreateTenantAccessTokenResponse: ...
    async def acreate(self, request: CreateTenantAccessTokenRequest, option: RequestOption | None = None) -> CreateTenantAccessTokenResponse: ...
    def internal(self, request: InternalTenantAccessTokenRequest, option: RequestOption | None = None) -> InternalTenantAccessTokenResponse: ...
    async def ainternal(self, request: InternalTenantAccessTokenRequest, option: RequestOption | None = None) -> InternalTenantAccessTokenResponse: ...
