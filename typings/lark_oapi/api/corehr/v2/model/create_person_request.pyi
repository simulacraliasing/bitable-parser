from .person_info import PersonInfo as PersonInfo
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreatePersonRequest(BaseRequest):
    client_token: str | None
    request_body: PersonInfo | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreatePersonRequestBuilder: ...

class CreatePersonRequestBuilder:
    def __init__(self) -> None: ...
    def client_token(self, client_token: str) -> CreatePersonRequestBuilder: ...
    def request_body(self, request_body: PersonInfo) -> CreatePersonRequestBuilder: ...
    def build(self) -> CreatePersonRequest: ...
