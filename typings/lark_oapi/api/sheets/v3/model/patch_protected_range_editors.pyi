from .protected_range_editors import ProtectedRangeEditors as ProtectedRangeEditors
from lark_oapi.core.construct import init as init

class PatchProtectedRangeEditors:
    type: str | None
    add_editors: ProtectedRangeEditors | None
    remove_editors: ProtectedRangeEditors | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchProtectedRangeEditorsBuilder: ...

class PatchProtectedRangeEditorsBuilder:
    def __init__(self) -> None: ...
    def type(self, type: str) -> PatchProtectedRangeEditorsBuilder: ...
    def add_editors(self, add_editors: ProtectedRangeEditors) -> PatchProtectedRangeEditorsBuilder: ...
    def remove_editors(self, remove_editors: ProtectedRangeEditors) -> PatchProtectedRangeEditorsBuilder: ...
    def build(self) -> PatchProtectedRangeEditors: ...
