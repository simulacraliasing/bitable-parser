from .enum import Enum as Enum
from lark_oapi.core.construct import init as init

class PhoneNumberAndAreaCode:
    area_code: Enum | None
    phone_number: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PhoneNumberAndAreaCodeBuilder: ...

class PhoneNumberAndAreaCodeBuilder:
    def __init__(self) -> None: ...
    def area_code(self, area_code: Enum) -> PhoneNumberAndAreaCodeBuilder: ...
    def phone_number(self, phone_number: str) -> PhoneNumberAndAreaCodeBuilder: ...
    def build(self) -> PhoneNumberAndAreaCode: ...
