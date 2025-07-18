from .get_country_region_response_body import GetCountryRegionResponseBody as GetCountryRegionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetCountryRegionResponse(BaseResponse):
    data: GetCountryRegionResponseBody | None
    def __init__(self, d=None) -> None: ...
