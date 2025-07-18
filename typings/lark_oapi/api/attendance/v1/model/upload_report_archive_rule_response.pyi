from .upload_report_archive_rule_response_body import UploadReportArchiveRuleResponseBody as UploadReportArchiveRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadReportArchiveRuleResponse(BaseResponse):
    data: UploadReportArchiveRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
