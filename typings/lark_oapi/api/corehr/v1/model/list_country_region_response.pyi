from .list_country_region_response_body import ListCountryRegionResponseBody as ListCountryRegionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCountryRegionResponse(BaseResponse):
    data: ListCountryRegionResponseBody | None
    def __init__(self, d=None) -> None: ...
