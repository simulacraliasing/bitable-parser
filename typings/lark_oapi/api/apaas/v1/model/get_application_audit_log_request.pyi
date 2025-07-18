from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetApplicationAuditLogRequest(BaseRequest):
    log_id: str | None
    namespace: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetApplicationAuditLogRequestBuilder: ...

class GetApplicationAuditLogRequestBuilder:
    def __init__(self) -> None: ...
    def log_id(self, log_id: str) -> GetApplicationAuditLogRequestBuilder: ...
    def namespace(self, namespace: str) -> GetApplicationAuditLogRequestBuilder: ...
    def build(self) -> GetApplicationAuditLogRequest: ...
