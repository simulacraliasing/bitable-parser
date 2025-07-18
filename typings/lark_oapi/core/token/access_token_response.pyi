from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AccessTokenResponse(BaseResponse):
    tenant_access_token: str | None
    app_access_token: str | None
    expire: int | None
    def __init__(self, d) -> None: ...
