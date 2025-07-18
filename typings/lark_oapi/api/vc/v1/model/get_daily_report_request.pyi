from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetDailyReportRequest(BaseRequest):
    start_time: int | None
    end_time: int | None
    unit: int | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetDailyReportRequestBuilder: ...

class GetDailyReportRequestBuilder:
    def __init__(self) -> None: ...
    def start_time(self, start_time: int) -> GetDailyReportRequestBuilder: ...
    def end_time(self, end_time: int) -> GetDailyReportRequestBuilder: ...
    def unit(self, unit: int) -> GetDailyReportRequestBuilder: ...
    def build(self) -> GetDailyReportRequest: ...
