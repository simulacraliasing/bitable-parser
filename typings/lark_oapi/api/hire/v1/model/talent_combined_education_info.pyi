from .talent_customized_data_object_value import TalentCustomizedDataObjectValue as TalentCustomizedDataObjectValue
from lark_oapi.core.construct import init as init

class TalentCombinedEducationInfo:
    id: str | None
    degree: int | None
    school: str | None
    field_of_study: str | None
    start_time: str | None
    end_time: str | None
    education_type: int | None
    academic_ranking: int | None
    customized_data: list[TalentCustomizedDataObjectValue] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TalentCombinedEducationInfoBuilder: ...

class TalentCombinedEducationInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> TalentCombinedEducationInfoBuilder: ...
    def degree(self, degree: int) -> TalentCombinedEducationInfoBuilder: ...
    def school(self, school: str) -> TalentCombinedEducationInfoBuilder: ...
    def field_of_study(self, field_of_study: str) -> TalentCombinedEducationInfoBuilder: ...
    def start_time(self, start_time: str) -> TalentCombinedEducationInfoBuilder: ...
    def end_time(self, end_time: str) -> TalentCombinedEducationInfoBuilder: ...
    def education_type(self, education_type: int) -> TalentCombinedEducationInfoBuilder: ...
    def academic_ranking(self, academic_ranking: int) -> TalentCombinedEducationInfoBuilder: ...
    def customized_data(self, customized_data: list[TalentCustomizedDataObjectValue]) -> TalentCombinedEducationInfoBuilder: ...
    def build(self) -> TalentCombinedEducationInfo: ...
