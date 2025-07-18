from .query_payment_detail_response_body import QueryPaymentDetailResponseBody as QueryPaymentDetailResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryPaymentDetailResponse(BaseResponse):
    data: QueryPaymentDetailResponseBody | None
    def __init__(self, d=None) -> None: ...
