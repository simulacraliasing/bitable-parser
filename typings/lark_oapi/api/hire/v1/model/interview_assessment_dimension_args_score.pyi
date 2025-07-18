from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class InterviewAssessmentDimensionArgsScore:
    id: str | None
    name: I18n | None
    description: I18n | None
    enabled: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InterviewAssessmentDimensionArgsScoreBuilder: ...

class InterviewAssessmentDimensionArgsScoreBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> InterviewAssessmentDimensionArgsScoreBuilder: ...
    def name(self, name: I18n) -> InterviewAssessmentDimensionArgsScoreBuilder: ...
    def description(self, description: I18n) -> InterviewAssessmentDimensionArgsScoreBuilder: ...
    def enabled(self, enabled: bool) -> InterviewAssessmentDimensionArgsScoreBuilder: ...
    def build(self) -> InterviewAssessmentDimensionArgsScore: ...
