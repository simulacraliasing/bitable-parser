from .list_ticket_message_response_body import ListTicketMessageResponseBody as ListTicketMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTicketMessageResponse(BaseResponse):
    data: ListTicketMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
