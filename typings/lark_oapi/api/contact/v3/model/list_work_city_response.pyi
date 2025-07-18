from .list_work_city_response_body import ListWorkCityResponseBody as ListWorkCityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListWorkCityResponse(BaseResponse):
    data: ListWorkCityResponseBody | None
    def __init__(self, d=None) -> None: ...
