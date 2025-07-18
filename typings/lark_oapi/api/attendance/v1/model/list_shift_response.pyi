from .list_shift_response_body import ListShiftResponseBody as ListShiftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListShiftResponse(BaseResponse):
    data: ListShiftResponseBody | None
    def __init__(self, d=None) -> None: ...
