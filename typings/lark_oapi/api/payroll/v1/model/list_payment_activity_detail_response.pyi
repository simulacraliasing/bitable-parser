from .list_payment_activity_detail_response_body import ListPaymentActivityDetailResponseBody as ListPaymentActivityDetailResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPaymentActivityDetailResponse(BaseResponse):
    data: ListPaymentActivityDetailResponseBody | None
    def __init__(self, d=None) -> None: ...
