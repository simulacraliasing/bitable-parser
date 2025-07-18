from .ability import Ability as Ability
from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class QuestionAssessment:
    question_type: int | None
    title: I18n | None
    description: I18n | None
    content: str | None
    abilities: list[Ability] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QuestionAssessmentBuilder: ...

class QuestionAssessmentBuilder:
    def __init__(self) -> None: ...
    def question_type(self, question_type: int) -> QuestionAssessmentBuilder: ...
    def title(self, title: I18n) -> QuestionAssessmentBuilder: ...
    def description(self, description: I18n) -> QuestionAssessmentBuilder: ...
    def content(self, content: str) -> QuestionAssessmentBuilder: ...
    def abilities(self, abilities: list[Ability]) -> QuestionAssessmentBuilder: ...
    def build(self) -> QuestionAssessment: ...
