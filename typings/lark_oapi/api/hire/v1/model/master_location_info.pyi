from lark_oapi.core.construct import init as init

class MasterLocationInfo:
    id: str | None
    zh_name: str | None
    en_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MasterLocationInfoBuilder: ...

class MasterLocationInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> MasterLocationInfoBuilder: ...
    def zh_name(self, zh_name: str) -> MasterLocationInfoBuilder: ...
    def en_name(self, en_name: str) -> MasterLocationInfoBuilder: ...
    def build(self) -> MasterLocationInfo: ...
