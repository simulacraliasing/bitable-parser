from .okr_progress_rate import OkrProgressRate as OkrProgressRate
from .text import Text as Text
from lark_oapi.core.construct import init as init

class OkrKeyResult:
    kr_id: int | None
    confidential: bool | None
    position: int | None
    score: int | None
    visible: bool | None
    weight: float | None
    progress_rate: OkrProgressRate | None
    content: Text | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OkrKeyResultBuilder: ...

class OkrKeyResultBuilder:
    def __init__(self) -> None: ...
    def kr_id(self, kr_id: int) -> OkrKeyResultBuilder: ...
    def confidential(self, confidential: bool) -> OkrKeyResultBuilder: ...
    def position(self, position: int) -> OkrKeyResultBuilder: ...
    def score(self, score: int) -> OkrKeyResultBuilder: ...
    def visible(self, visible: bool) -> OkrKeyResultBuilder: ...
    def weight(self, weight: float) -> OkrKeyResultBuilder: ...
    def progress_rate(self, progress_rate: OkrProgressRate) -> OkrKeyResultBuilder: ...
    def content(self, content: Text) -> OkrKeyResultBuilder: ...
    def build(self) -> OkrKeyResult: ...
