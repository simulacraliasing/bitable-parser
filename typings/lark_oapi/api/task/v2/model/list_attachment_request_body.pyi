from lark_oapi.core.construct import init as init

class ListAttachmentRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListAttachmentRequestBodyBuilder: ...

class ListAttachmentRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListAttachmentRequestBody: ...
