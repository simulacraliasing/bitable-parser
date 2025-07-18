from .search_basic_info_district_response_body import SearchBasicInfoDistrictResponseBody as SearchBasicInfoDistrictResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoDistrictResponse(BaseResponse):
    data: SearchBasicInfoDistrictResponseBody | None
    def __init__(self, d=None) -> None: ...
