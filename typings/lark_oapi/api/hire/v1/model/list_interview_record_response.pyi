from .list_interview_record_response_body import ListInterviewRecordResponseBody as ListInterviewRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInterviewRecordResponse(BaseResponse):
    data: ListInterviewRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
