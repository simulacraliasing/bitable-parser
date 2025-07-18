from .job_data import JobData as JobData
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchJobDataRequest(BaseRequest):
    client_token: str | None
    user_id_type: str | None
    department_id_type: str | None
    strict_verify: str | None
    job_data_id: str | None
    request_body: JobData | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchJobDataRequestBuilder: ...

class PatchJobDataRequestBuilder:
    def __init__(self) -> None: ...
    def client_token(self, client_token: str) -> PatchJobDataRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> PatchJobDataRequestBuilder: ...
    def department_id_type(self, department_id_type: str) -> PatchJobDataRequestBuilder: ...
    def strict_verify(self, strict_verify: str) -> PatchJobDataRequestBuilder: ...
    def job_data_id(self, job_data_id: str) -> PatchJobDataRequestBuilder: ...
    def request_body(self, request_body: JobData) -> PatchJobDataRequestBuilder: ...
    def build(self) -> PatchJobDataRequest: ...
