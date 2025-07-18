from .create_external_interview_response_body import CreateExternalInterviewResponseBody as CreateExternalInterviewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExternalInterviewResponse(BaseResponse):
    data: CreateExternalInterviewResponseBody | None
    def __init__(self, d=None) -> None: ...
