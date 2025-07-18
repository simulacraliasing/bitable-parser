from .create_access_token_response_body import CreateAccessTokenResponseBody as CreateAccessTokenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAccessTokenResponse(BaseResponse):
    data: CreateAccessTokenResponseBody | None
    def __init__(self, d=None) -> None: ...
