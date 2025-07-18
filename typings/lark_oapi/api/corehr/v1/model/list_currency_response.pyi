from .list_currency_response_body import ListCurrencyResponseBody as ListCurrencyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCurrencyResponse(BaseResponse):
    data: ListCurrencyResponseBody | None
    def __init__(self, d=None) -> None: ...
