from .verif_act_item_value import VerifActItemValue as VerifActItemValue
from lark_oapi.core.construct import init as init

class VerifActProration:
    start_date: str | None
    end_date: str | None
    cutoff_date: str | None
    item_values: list[VerifActItemValue] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> VerifActProrationBuilder: ...

class VerifActProrationBuilder:
    def __init__(self) -> None: ...
    def start_date(self, start_date: str) -> VerifActProrationBuilder: ...
    def end_date(self, end_date: str) -> VerifActProrationBuilder: ...
    def cutoff_date(self, cutoff_date: str) -> VerifActProrationBuilder: ...
    def item_values(self, item_values: list[VerifActItemValue]) -> VerifActProrationBuilder: ...
    def build(self) -> VerifActProration: ...
