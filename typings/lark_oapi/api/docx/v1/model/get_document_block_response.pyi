from .get_document_block_response_body import GetDocumentBlockResponseBody as GetDocumentBlockResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDocumentBlockResponse(BaseResponse):
    data: GetDocumentBlockResponseBody | None
    def __init__(self, d=None) -> None: ...
