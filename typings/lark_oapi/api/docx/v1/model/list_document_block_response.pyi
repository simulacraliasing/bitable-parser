from .list_document_block_response_body import ListDocumentBlockResponseBody as ListDocumentBlockResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListDocumentBlockResponse(BaseResponse):
    data: ListDocumentBlockResponseBody | None
    def __init__(self, d=None) -> None: ...
