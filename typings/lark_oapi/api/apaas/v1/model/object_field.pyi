from lark_oapi.core.construct import init as init

class ObjectField:
    id: int | None
    api_name: str | None
    type: str | None
    label: dict[str, str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ObjectFieldBuilder: ...

class ObjectFieldBuilder:
    def __init__(self) -> None: ...
    def id(self, id: int) -> ObjectFieldBuilder: ...
    def api_name(self, api_name: str) -> ObjectFieldBuilder: ...
    def type(self, type: str) -> ObjectFieldBuilder: ...
    def label(self, label: dict[str, str]) -> ObjectFieldBuilder: ...
    def build(self) -> ObjectField: ...
