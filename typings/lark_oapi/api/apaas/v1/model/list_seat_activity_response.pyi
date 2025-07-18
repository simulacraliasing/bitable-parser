from .list_seat_activity_response_body import ListSeatActivityResponseBody as ListSeatActivityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSeatActivityResponse(BaseResponse):
    data: ListSeatActivityResponseBody | None
    def __init__(self, d=None) -> None: ...
