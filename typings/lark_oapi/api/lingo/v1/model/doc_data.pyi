from .doc_content import DocContent as DocContent
from lark_oapi.core.construct import init as init

class DocData:
    doc_token: str | None
    created_at: int | None
    updated_at: int | None
    doc_contents: list[DocContent] | None
    root_content_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DocDataBuilder: ...

class DocDataBuilder:
    def __init__(self) -> None: ...
    def doc_token(self, doc_token: str) -> DocDataBuilder: ...
    def created_at(self, created_at: int) -> DocDataBuilder: ...
    def updated_at(self, updated_at: int) -> DocDataBuilder: ...
    def doc_contents(self, doc_contents: list[DocContent]) -> DocDataBuilder: ...
    def root_content_id(self, root_content_id: str) -> DocDataBuilder: ...
    def build(self) -> DocData: ...
