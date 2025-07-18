from .create_ticket_message_response_body import CreateTicketMessageResponseBody as CreateTicketMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTicketMessageResponse(BaseResponse):
    data: CreateTicketMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
