from .list_subregion_response_body import ListSubregionResponseBody as ListSubregionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSubregionResponse(BaseResponse):
    data: ListSubregionResponseBody | None
    def __init__(self, d=None) -> None: ...
