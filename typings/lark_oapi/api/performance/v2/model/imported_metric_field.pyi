from lark_oapi.core.construct import init as init

class ImportedMetricField:
    field_id: int | None
    field_value: str | None
    field_value_person: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ImportedMetricFieldBuilder: ...

class ImportedMetricFieldBuilder:
    def __init__(self) -> None: ...
    def field_id(self, field_id: int) -> ImportedMetricFieldBuilder: ...
    def field_value(self, field_value: str) -> ImportedMetricFieldBuilder: ...
    def field_value_person(self, field_value_person: str) -> ImportedMetricFieldBuilder: ...
    def build(self) -> ImportedMetricField: ...
