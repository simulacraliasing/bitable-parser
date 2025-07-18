from .submit_v2_offboarding_response_body import SubmitV2OffboardingResponseBody as SubmitV2OffboardingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SubmitV2OffboardingResponse(BaseResponse):
    data: SubmitV2OffboardingResponseBody | None
    def __init__(self, d=None) -> None: ...
