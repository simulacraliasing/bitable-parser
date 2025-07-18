from .attachment import Attachment as Attachment
from lark_oapi.core.construct import init as init

class UploadAttachmentResponseBody:
    items: list[Attachment] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UploadAttachmentResponseBodyBuilder: ...

class UploadAttachmentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[Attachment]) -> UploadAttachmentResponseBodyBuilder: ...
    def build(self) -> UploadAttachmentResponseBody: ...
