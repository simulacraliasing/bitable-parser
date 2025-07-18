from ..model.audit_log_list_application_audit_log_request import AuditLogListApplicationAuditLogRequest as AuditLogListApplicationAuditLogRequest
from ..model.audit_log_list_application_audit_log_response import AuditLogListApplicationAuditLogResponse as AuditLogListApplicationAuditLogResponse
from ..model.data_change_log_detail_application_audit_log_request import DataChangeLogDetailApplicationAuditLogRequest as DataChangeLogDetailApplicationAuditLogRequest
from ..model.data_change_log_detail_application_audit_log_response import DataChangeLogDetailApplicationAuditLogResponse as DataChangeLogDetailApplicationAuditLogResponse
from ..model.data_change_logs_list_application_audit_log_request import DataChangeLogsListApplicationAuditLogRequest as DataChangeLogsListApplicationAuditLogRequest
from ..model.data_change_logs_list_application_audit_log_response import DataChangeLogsListApplicationAuditLogResponse as DataChangeLogsListApplicationAuditLogResponse
from ..model.get_application_audit_log_request import GetApplicationAuditLogRequest as GetApplicationAuditLogRequest
from ..model.get_application_audit_log_response import GetApplicationAuditLogResponse as GetApplicationAuditLogResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ApplicationAuditLog:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def audit_log_list(self, request: AuditLogListApplicationAuditLogRequest, option: RequestOption | None = None) -> AuditLogListApplicationAuditLogResponse: ...
    async def aaudit_log_list(self, request: AuditLogListApplicationAuditLogRequest, option: RequestOption | None = None) -> AuditLogListApplicationAuditLogResponse: ...
    def data_change_log_detail(self, request: DataChangeLogDetailApplicationAuditLogRequest, option: RequestOption | None = None) -> DataChangeLogDetailApplicationAuditLogResponse: ...
    async def adata_change_log_detail(self, request: DataChangeLogDetailApplicationAuditLogRequest, option: RequestOption | None = None) -> DataChangeLogDetailApplicationAuditLogResponse: ...
    def data_change_logs_list(self, request: DataChangeLogsListApplicationAuditLogRequest, option: RequestOption | None = None) -> DataChangeLogsListApplicationAuditLogResponse: ...
    async def adata_change_logs_list(self, request: DataChangeLogsListApplicationAuditLogRequest, option: RequestOption | None = None) -> DataChangeLogsListApplicationAuditLogResponse: ...
    def get(self, request: GetApplicationAuditLogRequest, option: RequestOption | None = None) -> GetApplicationAuditLogResponse: ...
    async def aget(self, request: GetApplicationAuditLogRequest, option: RequestOption | None = None) -> GetApplicationAuditLogResponse: ...
