from lark_oapi.core.construct import init as init

class SchemaPredefineEnumStruct:
    name: str | None
    text: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SchemaPredefineEnumStructBuilder: ...

class SchemaPredefineEnumStructBuilder:
    def __init__(self) -> None: ...
    def name(self, name: str) -> SchemaPredefineEnumStructBuilder: ...
    def text(self, text: str) -> SchemaPredefineEnumStructBuilder: ...
    def build(self) -> SchemaPredefineEnumStruct: ...
