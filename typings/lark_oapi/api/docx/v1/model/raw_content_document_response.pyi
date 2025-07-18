from .raw_content_document_response_body import RawContentDocumentResponseBody as RawContentDocumentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RawContentDocumentResponse(BaseResponse):
    data: RawContentDocumentResponseBody | None
    def __init__(self, d=None) -> None: ...
