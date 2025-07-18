from .get_daily_report_response_body import GetDailyReportResponseBody as GetDailyReportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDailyReportResponse(BaseResponse):
    data: GetDailyReportResponseBody | None
    def __init__(self, d=None) -> None: ...
