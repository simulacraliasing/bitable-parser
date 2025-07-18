from .get_interview_record_response_body import GetInterviewRecordResponseBody as GetInterviewRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetInterviewRecordResponse(BaseResponse):
    data: GetInterviewRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
