from .complete_pre_hire_response_body import CompletePreHireResponseBody as CompletePreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CompletePreHireResponse(BaseResponse):
    data: CompletePreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
