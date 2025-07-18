from .audit_log_detail import AuditLogDetail as AuditLogDetail
from lark_oapi.core.construct import init as init

class GetApplicationAuditLogResponseBody:
    data: AuditLogDetail | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetApplicationAuditLogResponseBodyBuilder: ...

class GetApplicationAuditLogResponseBodyBuilder:
    def __init__(self) -> None: ...
    def data(self, data: AuditLogDetail) -> GetApplicationAuditLogResponseBodyBuilder: ...
    def build(self) -> GetApplicationAuditLogResponseBody: ...
