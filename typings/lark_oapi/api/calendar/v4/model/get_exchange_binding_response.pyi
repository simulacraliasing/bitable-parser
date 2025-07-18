from .get_exchange_binding_response_body import GetExchangeBindingResponseBody as GetExchangeBindingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetExchangeBindingResponse(BaseResponse):
    data: GetExchangeBindingResponseBody | None
    def __init__(self, d=None) -> None: ...
