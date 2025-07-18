from .query_shift_response_body import QueryShiftResponseBody as QueryShiftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryShiftResponse(BaseResponse):
    data: QueryShiftResponseBody | None
    def __init__(self, d=None) -> None: ...
