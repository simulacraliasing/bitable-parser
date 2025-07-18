from .list_payment_activity_response_body import ListPaymentActivityResponseBody as ListPaymentActivityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPaymentActivityResponse(BaseResponse):
    data: ListPaymentActivityResponseBody | None
    def __init__(self, d=None) -> None: ...
