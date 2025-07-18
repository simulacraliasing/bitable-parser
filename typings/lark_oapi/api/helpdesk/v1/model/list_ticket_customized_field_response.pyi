from .list_ticket_customized_field_response_body import ListTicketCustomizedFieldResponseBody as ListTicketCustomizedFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTicketCustomizedFieldResponse(BaseResponse):
    data: ListTicketCustomizedFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
