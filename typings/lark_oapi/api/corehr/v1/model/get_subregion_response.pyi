from .get_subregion_response_body import GetSubregionResponseBody as GetSubregionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSubregionResponse(BaseResponse):
    data: GetSubregionResponseBody | None
    def __init__(self, d=None) -> None: ...
