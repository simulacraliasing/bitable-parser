from .query_transfer_reason_response_body import QueryTransferReasonResponseBody as QueryTransferReasonResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryTransferReasonResponse(BaseResponse):
    data: QueryTransferReasonResponseBody | None
    def __init__(self, d=None) -> None: ...
