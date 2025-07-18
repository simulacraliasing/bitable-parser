from .get_application_audit_log_response_body import GetApplicationAuditLogResponseBody as GetApplicationAuditLogResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetApplicationAuditLogResponse(BaseResponse):
    data: GetApplicationAuditLogResponseBody | None
    def __init__(self, d=None) -> None: ...
