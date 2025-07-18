from .create_period_response_body import CreatePeriodResponseBody as CreatePeriodResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreatePeriodResponse(BaseResponse):
    data: CreatePeriodResponseBody | None
    def __init__(self, d=None) -> None: ...
