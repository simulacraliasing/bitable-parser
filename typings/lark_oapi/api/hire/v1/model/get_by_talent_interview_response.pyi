from .get_by_talent_interview_response_body import GetByTalentInterviewResponseBody as GetByTalentInterviewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetByTalentInterviewResponse(BaseResponse):
    data: GetByTalentInterviewResponseBody | None
    def __init__(self, d=None) -> None: ...
