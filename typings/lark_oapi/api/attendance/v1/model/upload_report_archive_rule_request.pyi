from .upload_report_archive_rule_request_body import UploadReportArchiveRuleRequestBody as UploadReportArchiveRuleRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UploadReportArchiveRuleRequest(BaseRequest):
    employee_type: str | None
    request_body: UploadReportArchiveRuleRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UploadReportArchiveRuleRequestBuilder: ...

class UploadReportArchiveRuleRequestBuilder:
    def __init__(self) -> None: ...
    def employee_type(self, employee_type: str) -> UploadReportArchiveRuleRequestBuilder: ...
    def request_body(self, request_body: UploadReportArchiveRuleRequestBody) -> UploadReportArchiveRuleRequestBuilder: ...
    def build(self) -> UploadReportArchiveRuleRequest: ...
