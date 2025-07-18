from .create_probation_assessment_response_body import CreateProbationAssessmentResponseBody as CreateProbationAssessmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateProbationAssessmentResponse(BaseResponse):
    data: CreateProbationAssessmentResponseBody | None
    def __init__(self, d=None) -> None: ...
