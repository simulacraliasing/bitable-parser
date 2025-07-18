from .search_basic_info_bank_response_body import SearchBasicInfoBankResponseBody as SearchBasicInfoBankResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoBankResponse(BaseResponse):
    data: SearchBasicInfoBankResponseBody | None
    def __init__(self, d=None) -> None: ...
