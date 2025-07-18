from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class InterviewDimensionScore:
    id: str | None
    name: I18n | None
    score_val: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InterviewDimensionScoreBuilder: ...

class InterviewDimensionScoreBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> InterviewDimensionScoreBuilder: ...
    def name(self, name: I18n) -> InterviewDimensionScoreBuilder: ...
    def score_val(self, score_val: int) -> InterviewDimensionScoreBuilder: ...
    def build(self) -> InterviewDimensionScore: ...
