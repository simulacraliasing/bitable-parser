from .data_validation_rule import DataValidationRule as DataValidationRule
from lark_oapi.core.construct import init as init

class DataValidation:
    data_validation_id: int | None
    data_validation_rule: DataValidationRule | None
    strict: str | None
    help_text: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DataValidationBuilder: ...

class DataValidationBuilder:
    def __init__(self) -> None: ...
    def data_validation_id(self, data_validation_id: int) -> DataValidationBuilder: ...
    def data_validation_rule(self, data_validation_rule: DataValidationRule) -> DataValidationBuilder: ...
    def strict(self, strict: str) -> DataValidationBuilder: ...
    def help_text(self, help_text: str) -> DataValidationBuilder: ...
    def build(self) -> DataValidation: ...
