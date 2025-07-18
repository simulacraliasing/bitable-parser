from .create_identity_response_body import CreateIdentityResponseBody as CreateIdentityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateIdentityResponse(BaseResponse):
    data: CreateIdentityResponseBody | None
    def __init__(self, d=None) -> None: ...
