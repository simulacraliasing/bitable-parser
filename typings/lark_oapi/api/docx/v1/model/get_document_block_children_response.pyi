from .get_document_block_children_response_body import GetDocumentBlockChildrenResponseBody as GetDocumentBlockChildrenResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDocumentBlockChildrenResponse(BaseResponse):
    data: GetDocumentBlockChildrenResponseBody | None
    def __init__(self, d=None) -> None: ...
