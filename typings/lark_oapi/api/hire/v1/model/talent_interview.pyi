from .interview_extend import InterviewExtend as InterviewExtend
from lark_oapi.core.construct import init as init

class TalentInterview:
    application_id: str | None
    interview_list: list[InterviewExtend] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TalentInterviewBuilder: ...

class TalentInterviewBuilder:
    def __init__(self) -> None: ...
    def application_id(self, application_id: str) -> TalentInterviewBuilder: ...
    def interview_list(self, interview_list: list[InterviewExtend]) -> TalentInterviewBuilder: ...
    def build(self) -> TalentInterview: ...
