from .get_ticket_customized_field_response_body import GetTicketCustomizedFieldResponseBody as GetTicketCustomizedFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetTicketCustomizedFieldResponse(BaseResponse):
    data: GetTicketCustomizedFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
