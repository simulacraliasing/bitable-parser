from .id_name_object import IdNameObject as IdNameObject
from lark_oapi.core.construct import init as init

class JobConfigRoundTypeResult:
    assessment_round: IdNameObject | None
    assessment_template: IdNameObject | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> JobConfigRoundTypeResultBuilder: ...

class JobConfigRoundTypeResultBuilder:
    def __init__(self) -> None: ...
    def assessment_round(self, assessment_round: IdNameObject) -> JobConfigRoundTypeResultBuilder: ...
    def assessment_template(self, assessment_template: IdNameObject) -> JobConfigRoundTypeResultBuilder: ...
    def build(self) -> JobConfigRoundTypeResult: ...
