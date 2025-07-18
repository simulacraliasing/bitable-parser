from .batch_create_user_daily_shift_response_body import BatchCreateUserDailyShiftResponseBody as BatchCreateUserDailyShiftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateUserDailyShiftResponse(BaseResponse):
    data: BatchCreateUserDailyShiftResponseBody | None
    def __init__(self, d=None) -> None: ...
