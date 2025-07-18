from .audit_log_list_application_audit_log_response_body import AuditLogListApplicationAuditLogResponseBody as AuditLogListApplicationAuditLogResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AuditLogListApplicationAuditLogResponse(BaseResponse):
    data: AuditLogListApplicationAuditLogResponseBody | None
    def __init__(self, d=None) -> None: ...
