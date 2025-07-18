from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class Subregion:
    id: str | None
    name: list[I18n] | None
    subdivision_id: str | None
    superior_subregion_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SubregionBuilder: ...

class SubregionBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> SubregionBuilder: ...
    def name(self, name: list[I18n]) -> SubregionBuilder: ...
    def subdivision_id(self, subdivision_id: str) -> SubregionBuilder: ...
    def superior_subregion_id(self, superior_subregion_id: str) -> SubregionBuilder: ...
    def build(self) -> Subregion: ...
