from .answer_user_query_ticket_request_body import AnswerUserQueryTicketRequestBody as AnswerUserQueryTicketRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class AnswerUserQueryTicketRequest(BaseRequest):
    ticket_id: str | None
    request_body: AnswerUserQueryTicketRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> AnswerUserQueryTicketRequestBuilder: ...

class AnswerUserQueryTicketRequestBuilder:
    def __init__(self) -> None: ...
    def ticket_id(self, ticket_id: str) -> AnswerUserQueryTicketRequestBuilder: ...
    def request_body(self, request_body: AnswerUserQueryTicketRequestBody) -> AnswerUserQueryTicketRequestBuilder: ...
    def build(self) -> AnswerUserQueryTicketRequest: ...
