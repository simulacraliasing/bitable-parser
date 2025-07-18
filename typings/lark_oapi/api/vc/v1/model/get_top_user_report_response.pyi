from .get_top_user_report_response_body import GetTopUserReportResponseBody as GetTopUserReportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetTopUserReportResponse(BaseResponse):
    data: GetTopUserReportResponseBody | None
    def __init__(self, d=None) -> None: ...
