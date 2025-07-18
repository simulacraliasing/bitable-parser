from .create_oidc_access_token_response_body import CreateOidcAccessTokenResponseBody as CreateOidcAccessTokenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateOidcAccessTokenResponse(BaseResponse):
    data: CreateOidcAccessTokenResponseBody | None
    def __init__(self, d=None) -> None: ...
