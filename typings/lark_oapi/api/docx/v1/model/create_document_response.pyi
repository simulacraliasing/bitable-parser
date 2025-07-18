from .create_document_response_body import CreateDocumentResponseBody as CreateDocumentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateDocumentResponse(BaseResponse):
    data: CreateDocumentResponseBody | None
    def __init__(self, d=None) -> None: ...
