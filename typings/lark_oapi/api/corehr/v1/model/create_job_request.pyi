from .job import Job as Job
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateJobRequest(BaseRequest):
    client_token: str | None
    request_body: Job | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateJobRequestBuilder: ...

class CreateJobRequestBuilder:
    def __init__(self) -> None: ...
    def client_token(self, client_token: str) -> CreateJobRequestBuilder: ...
    def request_body(self, request_body: Job) -> CreateJobRequestBuilder: ...
    def build(self) -> CreateJobRequest: ...
