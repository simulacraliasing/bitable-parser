from .query_transfer_type_response_body import QueryTransferTypeResponseBody as QueryTransferTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryTransferTypeResponse(BaseResponse):
    data: QueryTransferTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
