from .job_family import JobFamily as JobFamily
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateJobFamilyRequest(BaseRequest):
    request_body: JobFamily | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateJobFamilyRequestBuilder: ...

class CreateJobFamilyRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: JobFamily) -> CreateJobFamilyRequestBuilder: ...
    def build(self) -> CreateJobFamilyRequest: ...
