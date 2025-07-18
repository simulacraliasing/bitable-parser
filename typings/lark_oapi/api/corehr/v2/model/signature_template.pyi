from .signature_template_brief_info import SignatureTemplateBriefInfo as SignatureTemplateBriefInfo
from .signature_template_content_info import SignatureTemplateContentInfo as SignatureTemplateContentInfo
from lark_oapi.core.construct import init as init

class SignatureTemplate:
    id: str | None
    brief_info: SignatureTemplateBriefInfo | None
    content_info: SignatureTemplateContentInfo | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SignatureTemplateBuilder: ...

class SignatureTemplateBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> SignatureTemplateBuilder: ...
    def brief_info(self, brief_info: SignatureTemplateBriefInfo) -> SignatureTemplateBuilder: ...
    def content_info(self, content_info: SignatureTemplateContentInfo) -> SignatureTemplateBuilder: ...
    def build(self) -> SignatureTemplate: ...
