from .search_basic_info_city_response_body import SearchBasicInfoCityResponseBody as SearchBasicInfoCityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoCityResponse(BaseResponse):
    data: SearchBasicInfoCityResponseBody | None
    def __init__(self, d=None) -> None: ...
