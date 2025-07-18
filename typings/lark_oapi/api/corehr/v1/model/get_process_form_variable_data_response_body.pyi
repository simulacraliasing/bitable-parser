from .form_field_variable import FormFieldVariable as FormFieldVariable
from lark_oapi.core.construct import init as init

class GetProcessFormVariableDataResponseBody:
    field_variable_values: list[FormFieldVariable] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetProcessFormVariableDataResponseBodyBuilder: ...

class GetProcessFormVariableDataResponseBodyBuilder:
    def __init__(self) -> None: ...
    def field_variable_values(self, field_variable_values: list[FormFieldVariable]) -> GetProcessFormVariableDataResponseBodyBuilder: ...
    def build(self) -> GetProcessFormVariableDataResponseBody: ...
