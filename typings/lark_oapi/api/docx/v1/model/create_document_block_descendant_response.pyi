from .create_document_block_descendant_response_body import CreateDocumentBlockDescendantResponseBody as CreateDocumentBlockDescendantResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateDocumentBlockDescendantResponse(BaseResponse):
    data: CreateDocumentBlockDescendantResponseBody | None
    def __init__(self, d=None) -> None: ...
