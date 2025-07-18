from .customized_fields_ticket_response_body import CustomizedFieldsTicketResponseBody as CustomizedFieldsTicketResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CustomizedFieldsTicketResponse(BaseResponse):
    data: CustomizedFieldsTicketResponseBody | None
    def __init__(self, d=None) -> None: ...
