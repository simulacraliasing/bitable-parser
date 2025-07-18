from .list_period_response_body import ListPeriodResponseBody as ListPeriodResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPeriodResponse(BaseResponse):
    data: ListPeriodResponseBody | None
    def __init__(self, d=None) -> None: ...
