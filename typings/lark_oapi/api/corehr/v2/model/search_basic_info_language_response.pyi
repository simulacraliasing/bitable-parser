from .search_basic_info_language_response_body import SearchBasicInfoLanguageResponseBody as SearchBasicInfoLanguageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoLanguageResponse(BaseResponse):
    data: SearchBasicInfoLanguageResponseBody | None
    def __init__(self, d=None) -> None: ...
