from lark_oapi.core.construct import init as init

class CreateAttachmentRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateAttachmentRequestBodyBuilder: ...

class CreateAttachmentRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> CreateAttachmentRequestBody: ...
