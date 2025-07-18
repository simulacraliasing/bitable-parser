from .list_pin_response_body import ListPinResponseBody as ListPinResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPinResponse(BaseResponse):
    data: ListPinResponseBody | None
    def __init__(self, d=None) -> None: ...
