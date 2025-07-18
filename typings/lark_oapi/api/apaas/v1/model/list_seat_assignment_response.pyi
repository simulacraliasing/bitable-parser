from .list_seat_assignment_response_body import ListSeatAssignmentResponseBody as ListSeatAssignmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSeatAssignmentResponse(BaseResponse):
    data: ListSeatAssignmentResponseBody | None
    def __init__(self, d=None) -> None: ...
