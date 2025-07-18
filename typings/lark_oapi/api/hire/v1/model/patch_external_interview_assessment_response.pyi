from .patch_external_interview_assessment_response_body import PatchExternalInterviewAssessmentResponseBody as PatchExternalInterviewAssessmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchExternalInterviewAssessmentResponse(BaseResponse):
    data: PatchExternalInterviewAssessmentResponseBody | None
    def __init__(self, d=None) -> None: ...
