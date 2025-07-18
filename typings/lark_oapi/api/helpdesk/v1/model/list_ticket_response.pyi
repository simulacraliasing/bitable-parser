from .list_ticket_response_body import ListTicketResponseBody as ListTicketResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTicketResponse(BaseResponse):
    data: ListTicketResponseBody | None
    def __init__(self, d=None) -> None: ...
