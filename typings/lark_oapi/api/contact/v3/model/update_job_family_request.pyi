from .job_family import JobFamily as JobFamily
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UpdateJobFamilyRequest(BaseRequest):
    job_family_id: str | None
    request_body: JobFamily | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UpdateJobFamilyRequestBuilder: ...

class UpdateJobFamilyRequestBuilder:
    def __init__(self) -> None: ...
    def job_family_id(self, job_family_id: str) -> UpdateJobFamilyRequestBuilder: ...
    def request_body(self, request_body: JobFamily) -> UpdateJobFamilyRequestBuilder: ...
    def build(self) -> UpdateJobFamilyRequest: ...
