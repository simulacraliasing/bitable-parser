from .get_currency_response_body import GetCurrencyResponseBody as GetCurrencyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetCurrencyResponse(BaseResponse):
    data: GetCurrencyResponseBody | None
    def __init__(self, d=None) -> None: ...
