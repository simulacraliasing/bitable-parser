from .get_minute_statistics_response_body import GetMinuteStatisticsResponseBody as GetMinuteStatisticsResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMinuteStatisticsResponse(BaseResponse):
    data: GetMinuteStatisticsResponseBody | None
    def __init__(self, d=None) -> None: ...
