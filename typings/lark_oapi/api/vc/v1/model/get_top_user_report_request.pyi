from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetTopUserReportRequest(BaseRequest):
    start_time: int | None
    end_time: int | None
    limit: int | None
    order_by: int | None
    unit: int | None
    user_id_type: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetTopUserReportRequestBuilder: ...

class GetTopUserReportRequestBuilder:
    def __init__(self) -> None: ...
    def start_time(self, start_time: int) -> GetTopUserReportRequestBuilder: ...
    def end_time(self, end_time: int) -> GetTopUserReportRequestBuilder: ...
    def limit(self, limit: int) -> GetTopUserReportRequestBuilder: ...
    def order_by(self, order_by: int) -> GetTopUserReportRequestBuilder: ...
    def unit(self, unit: int) -> GetTopUserReportRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> GetTopUserReportRequestBuilder: ...
    def build(self) -> GetTopUserReportRequest: ...
