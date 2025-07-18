from .data_change_log_detail_application_audit_log_response_body import DataChangeLogDetailApplicationAuditLogResponseBody as DataChangeLogDetailApplicationAuditLogResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DataChangeLogDetailApplicationAuditLogResponse(BaseResponse):
    data: DataChangeLogDetailApplicationAuditLogResponseBody | None
    def __init__(self, d=None) -> None: ...
