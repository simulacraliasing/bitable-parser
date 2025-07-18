from .batch_query_meta_response_body import BatchQueryMetaResponseBody as BatchQueryMetaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryMetaResponse(BaseResponse):
    data: BatchQueryMetaResponseBody | None
    def __init__(self, d=None) -> None: ...
