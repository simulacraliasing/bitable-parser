from .job_grade_create import JobGradeCreate as JobGradeCreate
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateJobGradeRequest(BaseRequest):
    client_token: str | None
    request_body: JobGradeCreate | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateJobGradeRequestBuilder: ...

class CreateJobGradeRequestBuilder:
    def __init__(self) -> None: ...
    def client_token(self, client_token: str) -> CreateJobGradeRequestBuilder: ...
    def request_body(self, request_body: JobGradeCreate) -> CreateJobGradeRequestBuilder: ...
    def build(self) -> CreateJobGradeRequest: ...
