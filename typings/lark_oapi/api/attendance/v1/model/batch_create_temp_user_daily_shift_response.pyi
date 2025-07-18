from .batch_create_temp_user_daily_shift_response_body import BatchCreateTempUserDailyShiftResponseBody as BatchCreateTempUserDailyShiftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateTempUserDailyShiftResponse(BaseResponse):
    data: BatchCreateTempUserDailyShiftResponseBody | None
    def __init__(self, d=None) -> None: ...
