from ..model.get_daily_report_request import GetDailyReportRequest as GetDailyReportRequest
from ..model.get_daily_report_response import GetDailyReportResponse as GetDailyReportResponse
from ..model.get_top_user_report_request import GetTopUserReportRequest as GetTopUserReportRequest
from ..model.get_top_user_report_response import GetTopUserReportResponse as GetTopUserReportResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Report:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get_daily(self, request: GetDailyReportRequest, option: RequestOption | None = None) -> GetDailyReportResponse: ...
    async def aget_daily(self, request: GetDailyReportRequest, option: RequestOption | None = None) -> GetDailyReportResponse: ...
    def get_top_user(self, request: GetTopUserReportRequest, option: RequestOption | None = None) -> GetTopUserReportResponse: ...
    async def aget_top_user(self, request: GetTopUserReportRequest, option: RequestOption | None = None) -> GetTopUserReportResponse: ...
