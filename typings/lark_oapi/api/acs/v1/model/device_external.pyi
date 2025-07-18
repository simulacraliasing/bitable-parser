from lark_oapi.core.construct import init as init

class DeviceExternal:
    id: int | None
    name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeviceExternalBuilder: ...

class DeviceExternalBuilder:
    def __init__(self) -> None: ...
    def id(self, id: int) -> DeviceExternalBuilder: ...
    def name(self, name: str) -> DeviceExternalBuilder: ...
    def build(self) -> DeviceExternal: ...
