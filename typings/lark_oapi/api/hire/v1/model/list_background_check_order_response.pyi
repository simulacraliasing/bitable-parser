from .list_background_check_order_response_body import ListBackgroundCheckOrderResponseBody as ListBackgroundCheckOrderResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListBackgroundCheckOrderResponse(BaseResponse):
    data: ListBackgroundCheckOrderResponseBody | None
    def __init__(self, d=None) -> None: ...
