from lark_oapi.core.construct import init as init

class FormContent:
    field_id: str | None
    field_name: str | None
    field_value: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FormContentBuilder: ...

class FormContentBuilder:
    def __init__(self) -> None: ...
    def field_id(self, field_id: str) -> FormContentBuilder: ...
    def field_name(self, field_name: str) -> FormContentBuilder: ...
    def field_value(self, field_value: str) -> FormContentBuilder: ...
    def build(self) -> FormContent: ...
