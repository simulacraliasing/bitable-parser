from .enum import Enum as Enum
from .i18n import I18n as I18n
from .signature_signatory_label import SignatureSignatoryLabel as SignatureSignatoryLabel
from .signature_template_region_info import SignatureTemplateRegionInfo as SignatureTemplateRegionInfo
from .signature_template_setting import SignatureTemplateSetting as SignatureTemplateSetting
from lark_oapi.core.construct import init as init

class SignatureTemplateBriefInfo:
    id: str | None
    label: list[I18n] | None
    category: Enum | None
    usage: Enum | None
    signatory_labels: list[SignatureSignatoryLabel] | None
    active: bool | None
    create_by: str | None
    modify_by: str | None
    applicability: Enum | None
    creation_method: str | None
    version: str | None
    update_time: str | None
    create_time: str | None
    template_setting: SignatureTemplateSetting | None
    template_region_info: SignatureTemplateRegionInfo | None
    template_code: str | None
    template_desc: list[I18n] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SignatureTemplateBriefInfoBuilder: ...

class SignatureTemplateBriefInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> SignatureTemplateBriefInfoBuilder: ...
    def label(self, label: list[I18n]) -> SignatureTemplateBriefInfoBuilder: ...
    def category(self, category: Enum) -> SignatureTemplateBriefInfoBuilder: ...
    def usage(self, usage: Enum) -> SignatureTemplateBriefInfoBuilder: ...
    def signatory_labels(self, signatory_labels: list[SignatureSignatoryLabel]) -> SignatureTemplateBriefInfoBuilder: ...
    def active(self, active: bool) -> SignatureTemplateBriefInfoBuilder: ...
    def create_by(self, create_by: str) -> SignatureTemplateBriefInfoBuilder: ...
    def modify_by(self, modify_by: str) -> SignatureTemplateBriefInfoBuilder: ...
    def applicability(self, applicability: Enum) -> SignatureTemplateBriefInfoBuilder: ...
    def creation_method(self, creation_method: str) -> SignatureTemplateBriefInfoBuilder: ...
    def version(self, version: str) -> SignatureTemplateBriefInfoBuilder: ...
    def update_time(self, update_time: str) -> SignatureTemplateBriefInfoBuilder: ...
    def create_time(self, create_time: str) -> SignatureTemplateBriefInfoBuilder: ...
    def template_setting(self, template_setting: SignatureTemplateSetting) -> SignatureTemplateBriefInfoBuilder: ...
    def template_region_info(self, template_region_info: SignatureTemplateRegionInfo) -> SignatureTemplateBriefInfoBuilder: ...
    def template_code(self, template_code: str) -> SignatureTemplateBriefInfoBuilder: ...
    def template_desc(self, template_desc: list[I18n]) -> SignatureTemplateBriefInfoBuilder: ...
    def build(self) -> SignatureTemplateBriefInfo: ...
