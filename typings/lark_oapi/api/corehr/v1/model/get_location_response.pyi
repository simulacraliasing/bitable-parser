from .get_location_response_body import GetLocationResponseBody as GetLocationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetLocationResponse(BaseResponse):
    data: GetLocationResponseBody | None
    def __init__(self, d=None) -> None: ...
