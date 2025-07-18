from lark_oapi.core.construct import init as init

class ConnectorInstanceRefInfo:
    source_api_name: str | None
    source_type: str | None
    extra: dict[str, str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ConnectorInstanceRefInfoBuilder: ...

class ConnectorInstanceRefInfoBuilder:
    def __init__(self) -> None: ...
    def source_api_name(self, source_api_name: str) -> ConnectorInstanceRefInfoBuilder: ...
    def source_type(self, source_type: str) -> ConnectorInstanceRefInfoBuilder: ...
    def extra(self, extra: dict[str, str]) -> ConnectorInstanceRefInfoBuilder: ...
    def build(self) -> ConnectorInstanceRefInfo: ...
