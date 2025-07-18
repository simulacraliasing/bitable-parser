from .custom_field import CustomField as CustomField
from lark_oapi.core.construct import init as init

class GetByParamCustomFieldResponseBody:
    data: CustomField | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetByParamCustomFieldResponseBodyBuilder: ...

class GetByParamCustomFieldResponseBodyBuilder:
    def __init__(self) -> None: ...
    def data(self, data: CustomField) -> GetByParamCustomFieldResponseBodyBuilder: ...
    def build(self) -> GetByParamCustomFieldResponseBody: ...
