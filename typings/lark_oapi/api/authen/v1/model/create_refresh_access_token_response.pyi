from .create_refresh_access_token_response_body import CreateRefreshAccessTokenResponseBody as CreateRefreshAccessTokenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateRefreshAccessTokenResponse(BaseResponse):
    data: CreateRefreshAccessTokenResponseBody | None
    def __init__(self, d=None) -> None: ...
