from .document_cover import DocumentCover as DocumentCover
from lark_oapi.core.construct import init as init

class UpdateCoverRequest:
    cover: DocumentCover | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UpdateCoverRequestBuilder: ...

class UpdateCoverRequestBuilder:
    def __init__(self) -> None: ...
    def cover(self, cover: DocumentCover) -> UpdateCoverRequestBuilder: ...
    def build(self) -> UpdateCoverRequest: ...
