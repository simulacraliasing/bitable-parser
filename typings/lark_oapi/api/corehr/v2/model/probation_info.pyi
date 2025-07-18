from .assessment import Assessment as Assessment
from .custom_field_data import CustomFieldData as CustomFieldData
from .enum import Enum as Enum
from lark_oapi.core.construct import init as init

class ProbationInfo:
    employment_id: str | None
    probation_id: str | None
    probation_start_date: str | None
    probation_expected_end_date: str | None
    actual_probation_end_date: str | None
    initiating_time: str | None
    submission_type: Enum | None
    initiator_id: str | None
    probation_status: Enum | None
    self_review: str | None
    notes: str | None
    process_id: str | None
    converted_via_bpm: bool | None
    custom_fields: list[CustomFieldData] | None
    final_assessment_status: Enum | None
    final_assessment_result: Enum | None
    final_assessment_score: float | None
    final_assessment_grade: Enum | None
    final_assessment_comment: str | None
    final_assessment_detail: str | None
    assessments: list[Assessment] | None
    probation_extend_expected_end_date: str | None
    extended_probation_period_duration: int | None
    extended_probation_period_unit: Enum | None
    probation_outcome: Enum | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ProbationInfoBuilder: ...

class ProbationInfoBuilder:
    def __init__(self) -> None: ...
    def employment_id(self, employment_id: str) -> ProbationInfoBuilder: ...
    def probation_id(self, probation_id: str) -> ProbationInfoBuilder: ...
    def probation_start_date(self, probation_start_date: str) -> ProbationInfoBuilder: ...
    def probation_expected_end_date(self, probation_expected_end_date: str) -> ProbationInfoBuilder: ...
    def actual_probation_end_date(self, actual_probation_end_date: str) -> ProbationInfoBuilder: ...
    def initiating_time(self, initiating_time: str) -> ProbationInfoBuilder: ...
    def submission_type(self, submission_type: Enum) -> ProbationInfoBuilder: ...
    def initiator_id(self, initiator_id: str) -> ProbationInfoBuilder: ...
    def probation_status(self, probation_status: Enum) -> ProbationInfoBuilder: ...
    def self_review(self, self_review: str) -> ProbationInfoBuilder: ...
    def notes(self, notes: str) -> ProbationInfoBuilder: ...
    def process_id(self, process_id: str) -> ProbationInfoBuilder: ...
    def converted_via_bpm(self, converted_via_bpm: bool) -> ProbationInfoBuilder: ...
    def custom_fields(self, custom_fields: list[CustomFieldData]) -> ProbationInfoBuilder: ...
    def final_assessment_status(self, final_assessment_status: Enum) -> ProbationInfoBuilder: ...
    def final_assessment_result(self, final_assessment_result: Enum) -> ProbationInfoBuilder: ...
    def final_assessment_score(self, final_assessment_score: float) -> ProbationInfoBuilder: ...
    def final_assessment_grade(self, final_assessment_grade: Enum) -> ProbationInfoBuilder: ...
    def final_assessment_comment(self, final_assessment_comment: str) -> ProbationInfoBuilder: ...
    def final_assessment_detail(self, final_assessment_detail: str) -> ProbationInfoBuilder: ...
    def assessments(self, assessments: list[Assessment]) -> ProbationInfoBuilder: ...
    def probation_extend_expected_end_date(self, probation_extend_expected_end_date: str) -> ProbationInfoBuilder: ...
    def extended_probation_period_duration(self, extended_probation_period_duration: int) -> ProbationInfoBuilder: ...
    def extended_probation_period_unit(self, extended_probation_period_unit: Enum) -> ProbationInfoBuilder: ...
    def probation_outcome(self, probation_outcome: Enum) -> ProbationInfoBuilder: ...
    def build(self) -> ProbationInfo: ...
