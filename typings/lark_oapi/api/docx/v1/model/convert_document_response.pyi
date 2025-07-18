from .convert_document_response_body import ConvertDocumentResponseBody as ConvertDocumentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ConvertDocumentResponse(BaseResponse):
    data: ConvertDocumentResponseBody | None
    def __init__(self, d=None) -> None: ...
