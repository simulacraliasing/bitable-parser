from .get_interview_record_attachment_response_body import GetInterviewRecordAttachmentResponseBody as GetInterviewRecordAttachmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetInterviewRecordAttachmentResponse(BaseResponse):
    data: GetInterviewRecordAttachmentResponseBody | None
    def __init__(self, d=None) -> None: ...
