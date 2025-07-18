from lark_oapi.core.construct import init as init

class DataAssetImportKnowledgeLarkDoc:
    type: str | None
    token: str | None
    with_sub_docs: bool | None
    url: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DataAssetImportKnowledgeLarkDocBuilder: ...

class DataAssetImportKnowledgeLarkDocBuilder:
    def __init__(self) -> None: ...
    def type(self, type: str) -> DataAssetImportKnowledgeLarkDocBuilder: ...
    def token(self, token: str) -> DataAssetImportKnowledgeLarkDocBuilder: ...
    def with_sub_docs(self, with_sub_docs: bool) -> DataAssetImportKnowledgeLarkDocBuilder: ...
    def url(self, url: str) -> DataAssetImportKnowledgeLarkDocBuilder: ...
    def build(self) -> DataAssetImportKnowledgeLarkDoc: ...
