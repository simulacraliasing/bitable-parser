from lark_oapi.core.construct import init as init

class TargetMajorInfo:
    id: str | None
    zh_name: str | None
    en_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TargetMajorInfoBuilder: ...

class TargetMajorInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> TargetMajorInfoBuilder: ...
    def zh_name(self, zh_name: str) -> TargetMajorInfoBuilder: ...
    def en_name(self, en_name: str) -> TargetMajorInfoBuilder: ...
    def build(self) -> TargetMajorInfo: ...
