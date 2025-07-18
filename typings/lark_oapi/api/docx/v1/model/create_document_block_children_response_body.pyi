from .block import Block as Block
from lark_oapi.core.construct import init as init

class CreateDocumentBlockChildrenResponseBody:
    children: list[Block] | None
    document_revision_id: int | None
    client_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateDocumentBlockChildrenResponseBodyBuilder: ...

class CreateDocumentBlockChildrenResponseBodyBuilder:
    def __init__(self) -> None: ...
    def children(self, children: list[Block]) -> CreateDocumentBlockChildrenResponseBodyBuilder: ...
    def document_revision_id(self, document_revision_id: int) -> CreateDocumentBlockChildrenResponseBodyBuilder: ...
    def client_token(self, client_token: str) -> CreateDocumentBlockChildrenResponseBodyBuilder: ...
    def build(self) -> CreateDocumentBlockChildrenResponseBody: ...
