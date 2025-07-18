from .search_basic_info_currency_response_body import SearchBasicInfoCurrencyResponseBody as SearchBasicInfoCurrencyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoCurrencyResponse(BaseResponse):
    data: SearchBasicInfoCurrencyResponseBody | None
    def __init__(self, d=None) -> None: ...
