from .batch_delete_document_block_children_response_body import BatchDeleteDocumentBlockChildrenResponseBody as BatchDeleteDocumentBlockChildrenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDeleteDocumentBlockChildrenResponse(BaseResponse):
    data: BatchDeleteDocumentBlockChildrenResponseBody | None
    def __init__(self, d=None) -> None: ...
