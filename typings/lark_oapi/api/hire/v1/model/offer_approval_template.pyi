from .department import Department as Department
from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class OfferApprovalTemplate:
    id: str | None
    name: I18n | None
    create_time: str | None
    remark: str | None
    department_list: list[Department] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OfferApprovalTemplateBuilder: ...

class OfferApprovalTemplateBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> OfferApprovalTemplateBuilder: ...
    def name(self, name: I18n) -> OfferApprovalTemplateBuilder: ...
    def create_time(self, create_time: str) -> OfferApprovalTemplateBuilder: ...
    def remark(self, remark: str) -> OfferApprovalTemplateBuilder: ...
    def department_list(self, department_list: list[Department]) -> OfferApprovalTemplateBuilder: ...
    def build(self) -> OfferApprovalTemplate: ...
