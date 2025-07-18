from .code_name_object import CodeNameObject as CodeNameObject
from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class InterviewAddress:
    id: str | None
    name: I18n | None
    district: CodeNameObject | None
    city: CodeNameObject | None
    state: CodeNameObject | None
    country: CodeNameObject | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InterviewAddressBuilder: ...

class InterviewAddressBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> InterviewAddressBuilder: ...
    def name(self, name: I18n) -> InterviewAddressBuilder: ...
    def district(self, district: CodeNameObject) -> InterviewAddressBuilder: ...
    def city(self, city: CodeNameObject) -> InterviewAddressBuilder: ...
    def state(self, state: CodeNameObject) -> InterviewAddressBuilder: ...
    def country(self, country: CodeNameObject) -> InterviewAddressBuilder: ...
    def build(self) -> InterviewAddress: ...
