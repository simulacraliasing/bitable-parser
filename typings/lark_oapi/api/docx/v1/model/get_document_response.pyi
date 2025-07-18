from .get_document_response_body import GetDocumentResponseBody as GetDocumentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetDocumentResponse(BaseResponse):
    data: GetDocumentResponseBody | None
    def __init__(self, d=None) -> None: ...
