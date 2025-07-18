from .create_external_interview_assessment_response_body import CreateExternalInterviewAssessmentResponseBody as CreateExternalInterviewAssessmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExternalInterviewAssessmentResponse(BaseResponse):
    data: CreateExternalInterviewAssessmentResponseBody | None
    def __init__(self, d=None) -> None: ...
