from .okr_progress_rate import OkrProgressRate as OkrProgressRate
from .text import Text as Text
from lark_oapi.core.construct import init as init

class OkrObjective:
    objective_id: int | None
    confidential: bool | None
    position: int | None
    score: int | None
    visible: bool | None
    weight: float | None
    progress_rate: OkrProgressRate | None
    content: Text | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OkrObjectiveBuilder: ...

class OkrObjectiveBuilder:
    def __init__(self) -> None: ...
    def objective_id(self, objective_id: int) -> OkrObjectiveBuilder: ...
    def confidential(self, confidential: bool) -> OkrObjectiveBuilder: ...
    def position(self, position: int) -> OkrObjectiveBuilder: ...
    def score(self, score: int) -> OkrObjectiveBuilder: ...
    def visible(self, visible: bool) -> OkrObjectiveBuilder: ...
    def weight(self, weight: float) -> OkrObjectiveBuilder: ...
    def progress_rate(self, progress_rate: OkrProgressRate) -> OkrObjectiveBuilder: ...
    def content(self, content: Text) -> OkrObjectiveBuilder: ...
    def build(self) -> OkrObjective: ...
