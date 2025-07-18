from .batch_update_document_block_response_body import BatchUpdateDocumentBlockResponseBody as BatchUpdateDocumentBlockResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchUpdateDocumentBlockResponse(BaseResponse):
    data: BatchUpdateDocumentBlockResponseBody | None
    def __init__(self, d=None) -> None: ...
