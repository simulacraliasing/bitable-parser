from lark_oapi.core.construct import init as init

class TalentCustomizedAttachment:
    file_id: str | None
    file_name: str | None
    content_type: str | None
    file_size: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TalentCustomizedAttachmentBuilder: ...

class TalentCustomizedAttachmentBuilder:
    def __init__(self) -> None: ...
    def file_id(self, file_id: str) -> TalentCustomizedAttachmentBuilder: ...
    def file_name(self, file_name: str) -> TalentCustomizedAttachmentBuilder: ...
    def content_type(self, content_type: str) -> TalentCustomizedAttachmentBuilder: ...
    def file_size(self, file_size: int) -> TalentCustomizedAttachmentBuilder: ...
    def build(self) -> TalentCustomizedAttachment: ...
