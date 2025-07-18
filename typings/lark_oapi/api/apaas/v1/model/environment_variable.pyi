from .label import Label as Label
from lark_oapi.core.construct import init as init

class EnvironmentVariable:
    api_name: str | None
    label: Label | None
    description: str | None
    value: str | None
    is_encrypted: bool | None
    object_api_name: str | None
    object_label: Label | None
    created_at: int | None
    updated_at: int | None
    type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EnvironmentVariableBuilder: ...

class EnvironmentVariableBuilder:
    def __init__(self) -> None: ...
    def api_name(self, api_name: str) -> EnvironmentVariableBuilder: ...
    def label(self, label: Label) -> EnvironmentVariableBuilder: ...
    def description(self, description: str) -> EnvironmentVariableBuilder: ...
    def value(self, value: str) -> EnvironmentVariableBuilder: ...
    def is_encrypted(self, is_encrypted: bool) -> EnvironmentVariableBuilder: ...
    def object_api_name(self, object_api_name: str) -> EnvironmentVariableBuilder: ...
    def object_label(self, object_label: Label) -> EnvironmentVariableBuilder: ...
    def created_at(self, created_at: int) -> EnvironmentVariableBuilder: ...
    def updated_at(self, updated_at: int) -> EnvironmentVariableBuilder: ...
    def type(self, type: str) -> EnvironmentVariableBuilder: ...
    def build(self) -> EnvironmentVariable: ...
