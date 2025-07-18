from .create_oidc_refresh_access_token_response_body import CreateOidcRefreshAccessTokenResponseBody as CreateOidcRefreshAccessTokenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateOidcRefreshAccessTokenResponse(BaseResponse):
    data: CreateOidcRefreshAccessTokenResponseBody | None
    def __init__(self, d=None) -> None: ...
