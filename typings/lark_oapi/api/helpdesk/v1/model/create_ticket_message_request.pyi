from .create_ticket_message_request_body import CreateTicketMessageRequestBody as CreateTicketMessageRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateTicketMessageRequest(BaseRequest):
    ticket_id: str | None
    request_body: CreateTicketMessageRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateTicketMessageRequestBuilder: ...

class CreateTicketMessageRequestBuilder:
    def __init__(self) -> None: ...
    def ticket_id(self, ticket_id: str) -> CreateTicketMessageRequestBuilder: ...
    def request_body(self, request_body: CreateTicketMessageRequestBody) -> CreateTicketMessageRequestBuilder: ...
    def build(self) -> CreateTicketMessageRequest: ...
