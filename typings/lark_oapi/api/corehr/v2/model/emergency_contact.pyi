from .address import Address as Address
from .custom_field_data import CustomFieldData as CustomFieldData
from .email import Email as Email
from .enum import Enum as Enum
from .person_name import PersonName as PersonName
from .phone import Phone as Phone
from lark_oapi.core.construct import init as init

class EmergencyContact:
    id: str | None
    name: PersonName | None
    relationship: Enum | None
    phone_ist: list[Phone] | None
    phone_list: list[Phone] | None
    legal_name: str | None
    custom_fields: list[CustomFieldData] | None
    address: Address | None
    email: Email | None
    is_primary: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EmergencyContactBuilder: ...

class EmergencyContactBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> EmergencyContactBuilder: ...
    def name(self, name: PersonName) -> EmergencyContactBuilder: ...
    def relationship(self, relationship: Enum) -> EmergencyContactBuilder: ...
    def phone_ist(self, phone_ist: list[Phone]) -> EmergencyContactBuilder: ...
    def phone_list(self, phone_list: list[Phone]) -> EmergencyContactBuilder: ...
    def legal_name(self, legal_name: str) -> EmergencyContactBuilder: ...
    def custom_fields(self, custom_fields: list[CustomFieldData]) -> EmergencyContactBuilder: ...
    def address(self, address: Address) -> EmergencyContactBuilder: ...
    def email(self, email: Email) -> EmergencyContactBuilder: ...
    def is_primary(self, is_primary: bool) -> EmergencyContactBuilder: ...
    def build(self) -> EmergencyContact: ...
