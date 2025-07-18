from .search_basic_info_country_region_subdivision_response_body import SearchBasicInfoCountryRegionSubdivisionResponseBody as SearchBasicInfoCountryRegionSubdivisionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoCountryRegionSubdivisionResponse(BaseResponse):
    data: SearchBasicInfoCountryRegionSubdivisionResponseBody | None
    def __init__(self, d=None) -> None: ...
