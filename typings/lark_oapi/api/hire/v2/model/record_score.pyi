from lark_oapi.core.construct import init as init

class RecordScore:
    score: float | None
    total_score: float | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RecordScoreBuilder: ...

class RecordScoreBuilder:
    def __init__(self) -> None: ...
    def score(self, score: float) -> RecordScoreBuilder: ...
    def total_score(self, total_score: float) -> RecordScoreBuilder: ...
    def build(self) -> RecordScore: ...
