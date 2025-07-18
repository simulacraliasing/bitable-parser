from lark_oapi.core.construct import init as init

class AssessmentForCreate:
    assessment_status: str | None
    assessment_result: str | None
    assessment_score: float | None
    assessment_grade: str | None
    assessment_comment: str | None
    assessment_detail: str | None
    is_final_asssessment: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AssessmentForCreateBuilder: ...

class AssessmentForCreateBuilder:
    def __init__(self) -> None: ...
    def assessment_status(self, assessment_status: str) -> AssessmentForCreateBuilder: ...
    def assessment_result(self, assessment_result: str) -> AssessmentForCreateBuilder: ...
    def assessment_score(self, assessment_score: float) -> AssessmentForCreateBuilder: ...
    def assessment_grade(self, assessment_grade: str) -> AssessmentForCreateBuilder: ...
    def assessment_comment(self, assessment_comment: str) -> AssessmentForCreateBuilder: ...
    def assessment_detail(self, assessment_detail: str) -> AssessmentForCreateBuilder: ...
    def is_final_asssessment(self, is_final_asssessment: bool) -> AssessmentForCreateBuilder: ...
    def build(self) -> AssessmentForCreate: ...
