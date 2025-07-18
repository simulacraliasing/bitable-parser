from .data_validation_value import DataValidationValue as DataValidationValue
from .option_properties import OptionProperties as OptionProperties
from lark_oapi.core.construct import init as init

class SingleOption:
    type: str | None
    range: str | None
    data_validation_values: list[DataValidationValue] | None
    properties: OptionProperties | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SingleOptionBuilder: ...

class SingleOptionBuilder:
    def __init__(self) -> None: ...
    def type(self, type: str) -> SingleOptionBuilder: ...
    def range(self, range: str) -> SingleOptionBuilder: ...
    def data_validation_values(self, data_validation_values: list[DataValidationValue]) -> SingleOptionBuilder: ...
    def properties(self, properties: OptionProperties) -> SingleOptionBuilder: ...
    def build(self) -> SingleOption: ...
