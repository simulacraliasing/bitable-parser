from lark_oapi.core.cache import *
from .access_token_response import AccessTokenResponse as AccessTokenResponse
from .create_isv_app_token_request import CreateIsvAppTokenRequest as CreateIsvAppTokenRequest
from .create_isv_tenant_token_request import CreateIsvTenantTokenRequest as CreateIsvTenantTokenRequest
from .create_self_app_token_request import CreateSelfAppTokenRequest as CreateSelfAppTokenRequest
from .create_self_tenant_token_request import CreateSelfTenantTokenRequest as CreateSelfTenantTokenRequest
from .create_token_request_body import CreateTokenRequestBody as CreateTokenRequestBody
from lark_oapi.core import JSON as JSON, Strings as Strings
from lark_oapi.core.const import UTF_8 as UTF_8
from lark_oapi.core.exception import ObtainAccessTokenException as ObtainAccessTokenException
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse

class TokenManager:
    cache: ICache
    @staticmethod
    def get_self_app_token(conf: Config) -> str: ...
    @staticmethod
    def get_self_tenant_token(config: Config) -> str: ...
    @staticmethod
    def get_isv_app_token(config: Config, app_ticket: str) -> str: ...
    @staticmethod
    def get_isv_tenant_token(config: Config, tenant_key: str, app_ticket: str) -> str: ...
