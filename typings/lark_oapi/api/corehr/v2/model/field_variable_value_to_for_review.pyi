from .field_variable_value_i18n import FieldVariableValueI18n as FieldVariableValueI18n
from .field_variable_value_to_file_for_write import FieldVariableValueToFileForWrite as FieldVariableValueToFileForWrite
from .field_variable_value_to_object import FieldVariableValueToObject as FieldVariableValueToObject
from .field_variable_value_to_record import FieldVariableValueToRecord as FieldVariableValueToRecord
from lark_oapi.core.construct import init as init

class FieldVariableValueToForReview:
    text_value: str | None
    bool_value: bool | None
    number_value: str | None
    enum_value: str | None
    date_value: str | None
    date_time_value: str | None
    i18n_value: FieldVariableValueI18n | None
    object_value: FieldVariableValueToObject | None
    department_value: str | None
    employment_value: str | None
    list_values: list[str] | None
    file_value: FieldVariableValueToFileForWrite | None
    record_values: list[FieldVariableValueToRecord] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FieldVariableValueToForReviewBuilder: ...

class FieldVariableValueToForReviewBuilder:
    def __init__(self) -> None: ...
    def text_value(self, text_value: str) -> FieldVariableValueToForReviewBuilder: ...
    def bool_value(self, bool_value: bool) -> FieldVariableValueToForReviewBuilder: ...
    def number_value(self, number_value: str) -> FieldVariableValueToForReviewBuilder: ...
    def enum_value(self, enum_value: str) -> FieldVariableValueToForReviewBuilder: ...
    def date_value(self, date_value: str) -> FieldVariableValueToForReviewBuilder: ...
    def date_time_value(self, date_time_value: str) -> FieldVariableValueToForReviewBuilder: ...
    def i18n_value(self, i18n_value: FieldVariableValueI18n) -> FieldVariableValueToForReviewBuilder: ...
    def object_value(self, object_value: FieldVariableValueToObject) -> FieldVariableValueToForReviewBuilder: ...
    def department_value(self, department_value: str) -> FieldVariableValueToForReviewBuilder: ...
    def employment_value(self, employment_value: str) -> FieldVariableValueToForReviewBuilder: ...
    def list_values(self, list_values: list[str]) -> FieldVariableValueToForReviewBuilder: ...
    def file_value(self, file_value: FieldVariableValueToFileForWrite) -> FieldVariableValueToForReviewBuilder: ...
    def record_values(self, record_values: list[FieldVariableValueToRecord]) -> FieldVariableValueToForReviewBuilder: ...
    def build(self) -> FieldVariableValueToForReview: ...
