from .enum import Enum as Enum
from lark_oapi.core.construct import init as init

class Assessment:
    assessment_id: str | None
    assessment_status: Enum | None
    assessment_result: Enum | None
    assessment_score: float | None
    assessment_grade: Enum | None
    assessment_comment: str | None
    assessment_detail: str | None
    is_final_asssessment: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AssessmentBuilder: ...

class AssessmentBuilder:
    def __init__(self) -> None: ...
    def assessment_id(self, assessment_id: str) -> AssessmentBuilder: ...
    def assessment_status(self, assessment_status: Enum) -> AssessmentBuilder: ...
    def assessment_result(self, assessment_result: Enum) -> AssessmentBuilder: ...
    def assessment_score(self, assessment_score: float) -> AssessmentBuilder: ...
    def assessment_grade(self, assessment_grade: Enum) -> AssessmentBuilder: ...
    def assessment_comment(self, assessment_comment: str) -> AssessmentBuilder: ...
    def assessment_detail(self, assessment_detail: str) -> AssessmentBuilder: ...
    def is_final_asssessment(self, is_final_asssessment: bool) -> AssessmentBuilder: ...
    def build(self) -> Assessment: ...
