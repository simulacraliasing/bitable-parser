from .get_ticket_response_body import GetTicketResponseBody as GetTicketResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetTicketResponse(BaseResponse):
    data: GetTicketResponseBody | None
    def __init__(self, d=None) -> None: ...
