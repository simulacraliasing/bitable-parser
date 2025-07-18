from .probation_info_for_submit import ProbationInfoForSubmit as ProbationInfoForSubmit
from lark_oapi.core.construct import init as init

class SubmitProbationResponseBody:
    probation_info: ProbationInfoForSubmit | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SubmitProbationResponseBodyBuilder: ...

class SubmitProbationResponseBodyBuilder:
    def __init__(self) -> None: ...
    def probation_info(self, probation_info: ProbationInfoForSubmit) -> SubmitProbationResponseBodyBuilder: ...
    def build(self) -> SubmitProbationResponseBody: ...
