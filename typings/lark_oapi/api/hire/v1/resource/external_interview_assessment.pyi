from ..model.create_external_interview_assessment_request import CreateExternalInterviewAssessmentRequest as CreateExternalInterviewAssessmentRequest
from ..model.create_external_interview_assessment_response import CreateExternalInterviewAssessmentResponse as CreateExternalInterviewAssessmentResponse
from ..model.patch_external_interview_assessment_request import PatchExternalInterviewAssessmentRequest as PatchExternalInterviewAssessmentRequest
from ..model.patch_external_interview_assessment_response import PatchExternalInterviewAssessmentResponse as PatchExternalInterviewAssessmentResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ExternalInterviewAssessment:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateExternalInterviewAssessmentRequest, option: RequestOption | None = None) -> CreateExternalInterviewAssessmentResponse: ...
    async def acreate(self, request: CreateExternalInterviewAssessmentRequest, option: RequestOption | None = None) -> CreateExternalInterviewAssessmentResponse: ...
    def patch(self, request: PatchExternalInterviewAssessmentRequest, option: RequestOption | None = None) -> PatchExternalInterviewAssessmentResponse: ...
    async def apatch(self, request: PatchExternalInterviewAssessmentRequest, option: RequestOption | None = None) -> PatchExternalInterviewAssessmentResponse: ...
