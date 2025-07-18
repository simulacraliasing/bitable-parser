from .create_document_block_children_response_body import CreateDocumentBlockChildrenResponseBody as CreateDocumentBlockChildrenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateDocumentBlockChildrenResponse(BaseResponse):
    data: CreateDocumentBlockChildrenResponseBody | None
    def __init__(self, d=None) -> None: ...
