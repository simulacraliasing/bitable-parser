from .custom_field import CustomField as CustomField
from lark_oapi.core.construct import init as init

class GetCustomFieldResponseBody:
    custom_field: CustomField | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetCustomFieldResponseBodyBuilder: ...

class GetCustomFieldResponseBodyBuilder:
    def __init__(self) -> None: ...
    def custom_field(self, custom_field: CustomField) -> GetCustomFieldResponseBodyBuilder: ...
    def build(self) -> GetCustomFieldResponseBody: ...
