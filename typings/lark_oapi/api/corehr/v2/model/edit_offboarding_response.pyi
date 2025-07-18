from .edit_offboarding_response_body import EditOffboardingResponseBody as EditOffboardingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class EditOffboardingResponse(BaseResponse):
    data: EditOffboardingResponseBody | None
    def __init__(self, d=None) -> None: ...
