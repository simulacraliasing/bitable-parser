from .update_external_interview_response_body import UpdateExternalInterviewResponseBody as UpdateExternalInterviewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateExternalInterviewResponse(BaseResponse):
    data: UpdateExternalInterviewResponseBody | None
    def __init__(self, d=None) -> None: ...
