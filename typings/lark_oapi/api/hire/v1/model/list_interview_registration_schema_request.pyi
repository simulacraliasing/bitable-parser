from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListInterviewRegistrationSchemaRequest(BaseRequest):
    page_token: str | None
    page_size: int | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListInterviewRegistrationSchemaRequestBuilder: ...

class ListInterviewRegistrationSchemaRequestBuilder:
    def __init__(self) -> None: ...
    def page_token(self, page_token: str) -> ListInterviewRegistrationSchemaRequestBuilder: ...
    def page_size(self, page_size: int) -> ListInterviewRegistrationSchemaRequestBuilder: ...
    def build(self) -> ListInterviewRegistrationSchemaRequest: ...
