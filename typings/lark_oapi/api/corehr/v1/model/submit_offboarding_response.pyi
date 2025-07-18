from .submit_offboarding_response_body import SubmitOffboardingResponseBody as SubmitOffboardingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SubmitOffboardingResponse(BaseResponse):
    data: SubmitOffboardingResponseBody | None
    def __init__(self, d=None) -> None: ...
