from .create_document_request_body import CreateDocumentRequestBody as CreateDocumentRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateDocumentRequest(BaseRequest):
    request_body: CreateDocumentRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateDocumentRequestBuilder: ...

class CreateDocumentRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: CreateDocumentRequestBody) -> CreateDocumentRequestBuilder: ...
    def build(self) -> CreateDocumentRequest: ...
