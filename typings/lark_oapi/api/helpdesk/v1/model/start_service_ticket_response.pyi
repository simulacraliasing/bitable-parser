from .start_service_ticket_response_body import StartServiceTicketResponseBody as StartServiceTicketResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class StartServiceTicketResponse(BaseResponse):
    data: StartServiceTicketResponseBody | None
    def __init__(self, d=None) -> None: ...
