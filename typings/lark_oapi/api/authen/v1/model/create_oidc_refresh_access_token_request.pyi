from .create_oidc_refresh_access_token_request_body import CreateOidcRefreshAccessTokenRequestBody as CreateOidcRefreshAccessTokenRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateOidcRefreshAccessTokenRequest(BaseRequest):
    request_body: CreateOidcRefreshAccessTokenRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateOidcRefreshAccessTokenRequestBuilder: ...

class CreateOidcRefreshAccessTokenRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: CreateOidcRefreshAccessTokenRequestBody) -> CreateOidcRefreshAccessTokenRequestBuilder: ...
    def build(self) -> CreateOidcRefreshAccessTokenRequest: ...
