from lark_oapi.core.construct import init as init

class CreateDocumentRequestBody:
    folder_token: str | None
    title: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateDocumentRequestBodyBuilder: ...

class CreateDocumentRequestBodyBuilder:
    def __init__(self) -> None: ...
    def folder_token(self, folder_token: str) -> CreateDocumentRequestBodyBuilder: ...
    def title(self, title: str) -> CreateDocumentRequestBodyBuilder: ...
    def build(self) -> CreateDocumentRequestBody: ...
