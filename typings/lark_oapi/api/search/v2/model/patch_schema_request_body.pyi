from .patch_schema_property import PatchSchemaProperty as PatchSchemaProperty
from .schema_display import SchemaDisplay as SchemaDisplay
from lark_oapi.core.construct import init as init

class PatchSchemaRequestBody:
    display: SchemaDisplay | None
    properties: list[PatchSchemaProperty] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchSchemaRequestBodyBuilder: ...

class PatchSchemaRequestBodyBuilder:
    def __init__(self) -> None: ...
    def display(self, display: SchemaDisplay) -> PatchSchemaRequestBodyBuilder: ...
    def properties(self, properties: list[PatchSchemaProperty]) -> PatchSchemaRequestBodyBuilder: ...
    def build(self) -> PatchSchemaRequestBody: ...
