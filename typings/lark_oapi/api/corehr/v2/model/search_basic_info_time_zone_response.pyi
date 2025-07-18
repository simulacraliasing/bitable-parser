from .search_basic_info_time_zone_response_body import SearchBasicInfoTimeZoneResponseBody as SearchBasicInfoTimeZoneResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoTimeZoneResponse(BaseResponse):
    data: SearchBasicInfoTimeZoneResponseBody | None
    def __init__(self, d=None) -> None: ...
