from lark_oapi.core.construct import init as init

class ExternalBackgroundCheckAttachment:
    id: str | None
    name: str | None
    size: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ExternalBackgroundCheckAttachmentBuilder: ...

class ExternalBackgroundCheckAttachmentBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> ExternalBackgroundCheckAttachmentBuilder: ...
    def name(self, name: str) -> ExternalBackgroundCheckAttachmentBuilder: ...
    def size(self, size: int) -> ExternalBackgroundCheckAttachmentBuilder: ...
    def build(self) -> ExternalBackgroundCheckAttachment: ...
