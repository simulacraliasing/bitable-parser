from .get_verification_response_body import GetVerificationResponseBody as GetVerificationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetVerificationResponse(BaseResponse):
    data: GetVerificationResponseBody | None
    def __init__(self, d=None) -> None: ...
