from .search_basic_info_country_region_response_body import SearchBasicInfoCountryRegionResponseBody as SearchBasicInfoCountryRegionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoCountryRegionResponse(BaseResponse):
    data: SearchBasicInfoCountryRegionResponseBody | None
    def __init__(self, d=None) -> None: ...
