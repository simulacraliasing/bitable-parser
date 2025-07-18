from .get_work_city_response_body import GetWorkCityResponseBody as GetWorkCityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetWorkCityResponse(BaseResponse):
    data: GetWorkCityResponseBody | None
    def __init__(self, d=None) -> None: ...
