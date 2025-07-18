from lark_oapi.core.construct import init as init

class ApplicationTalentAttachmentResumeInfo:
    id: str | None
    name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ApplicationTalentAttachmentResumeInfoBuilder: ...

class ApplicationTalentAttachmentResumeInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> ApplicationTalentAttachmentResumeInfoBuilder: ...
    def name(self, name: str) -> ApplicationTalentAttachmentResumeInfoBuilder: ...
    def build(self) -> ApplicationTalentAttachmentResumeInfo: ...
