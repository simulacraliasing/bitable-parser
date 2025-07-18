from .create_exchange_binding_response_body import CreateExchangeBindingResponseBody as CreateExchangeBindingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExchangeBindingResponse(BaseResponse):
    data: CreateExchangeBindingResponseBody | None
    def __init__(self, d=None) -> None: ...
