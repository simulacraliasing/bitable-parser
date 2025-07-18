from lark_oapi.core.construct import init as init

class InterviewAttachment:
    file_id: str | None
    file_name: str | None
    content_type: str | None
    create_time: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InterviewAttachmentBuilder: ...

class InterviewAttachmentBuilder:
    def __init__(self) -> None: ...
    def file_id(self, file_id: str) -> InterviewAttachmentBuilder: ...
    def file_name(self, file_name: str) -> InterviewAttachmentBuilder: ...
    def content_type(self, content_type: str) -> InterviewAttachmentBuilder: ...
    def create_time(self, create_time: str) -> InterviewAttachmentBuilder: ...
    def build(self) -> InterviewAttachment: ...
