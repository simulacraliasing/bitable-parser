from .list_indicator_response_body import ListIndicatorResponseBody as ListIndicatorResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListIndicatorResponse(BaseResponse):
    data: ListIndicatorResponseBody | None
    def __init__(self, d=None) -> None: ...
