from .code_name_object import CodeNameObject as CodeNameObject
from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class CommonAddress:
    id: str | None
    name: I18n | None
    district: CodeNameObject | None
    city: CodeNameObject | None
    state: CodeNameObject | None
    country: CodeNameObject | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CommonAddressBuilder: ...

class CommonAddressBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> CommonAddressBuilder: ...
    def name(self, name: I18n) -> CommonAddressBuilder: ...
    def district(self, district: CodeNameObject) -> CommonAddressBuilder: ...
    def city(self, city: CodeNameObject) -> CommonAddressBuilder: ...
    def state(self, state: CodeNameObject) -> CommonAddressBuilder: ...
    def country(self, country: CodeNameObject) -> CommonAddressBuilder: ...
    def build(self) -> CommonAddress: ...
