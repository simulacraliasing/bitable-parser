from .query_user_daily_shift_response_body import QueryUserDailyShiftResponseBody as QueryUserDailyShiftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserDailyShiftResponse(BaseResponse):
    data: QueryUserDailyShiftResponseBody | None
    def __init__(self, d=None) -> None: ...
