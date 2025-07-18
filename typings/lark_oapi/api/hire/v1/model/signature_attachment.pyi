from lark_oapi.core.construct import init as init

class SignatureAttachment:
    id: str | None
    file_name: str | None
    file_template_id: str | None
    file_template_name: str | None
    file_template_type_id: str | None
    file_template_type_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SignatureAttachmentBuilder: ...

class SignatureAttachmentBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> SignatureAttachmentBuilder: ...
    def file_name(self, file_name: str) -> SignatureAttachmentBuilder: ...
    def file_template_id(self, file_template_id: str) -> SignatureAttachmentBuilder: ...
    def file_template_name(self, file_template_name: str) -> SignatureAttachmentBuilder: ...
    def file_template_type_id(self, file_template_type_id: str) -> SignatureAttachmentBuilder: ...
    def file_template_type_name(self, file_template_type_name: str) -> SignatureAttachmentBuilder: ...
    def build(self) -> SignatureAttachment: ...
