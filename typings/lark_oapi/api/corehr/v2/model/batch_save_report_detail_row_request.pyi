from .report_detail_req import ReportDetailReq as ReportDetailReq
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class BatchSaveReportDetailRowRequest(BaseRequest):
    request_body: ReportDetailReq | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> BatchSaveReportDetailRowRequestBuilder: ...

class BatchSaveReportDetailRowRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: ReportDetailReq) -> BatchSaveReportDetailRowRequestBuilder: ...
    def build(self) -> BatchSaveReportDetailRowRequest: ...
