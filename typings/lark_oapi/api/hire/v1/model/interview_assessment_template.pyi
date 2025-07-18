from .i18n import I18n as I18n
from .interview_assessment_template_args import InterviewAssessmentTemplateArgs as InterviewAssessmentTemplateArgs
from lark_oapi.core.construct import init as init

class InterviewAssessmentTemplate:
    id: str | None
    name: I18n | None
    args: InterviewAssessmentTemplateArgs | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InterviewAssessmentTemplateBuilder: ...

class InterviewAssessmentTemplateBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> InterviewAssessmentTemplateBuilder: ...
    def name(self, name: I18n) -> InterviewAssessmentTemplateBuilder: ...
    def args(self, args: InterviewAssessmentTemplateArgs) -> InterviewAssessmentTemplateBuilder: ...
    def build(self) -> InterviewAssessmentTemplate: ...
