from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListSeatAssignmentRequest(BaseRequest):
    seat_type: str | None
    page_size: str | None
    page_token: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListSeatAssignmentRequestBuilder: ...

class ListSeatAssignmentRequestBuilder:
    def __init__(self) -> None: ...
    def seat_type(self, seat_type: str) -> ListSeatAssignmentRequestBuilder: ...
    def page_size(self, page_size: str) -> ListSeatAssignmentRequestBuilder: ...
    def page_token(self, page_token: str) -> ListSeatAssignmentRequestBuilder: ...
    def build(self) -> ListSeatAssignmentRequest: ...
