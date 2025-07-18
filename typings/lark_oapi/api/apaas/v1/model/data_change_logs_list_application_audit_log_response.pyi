from .data_change_logs_list_application_audit_log_response_body import DataChangeLogsListApplicationAuditLogResponseBody as DataChangeLogsListApplicationAuditLogResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DataChangeLogsListApplicationAuditLogResponse(BaseResponse):
    data: DataChangeLogsListApplicationAuditLogResponseBody | None
    def __init__(self, d=None) -> None: ...
