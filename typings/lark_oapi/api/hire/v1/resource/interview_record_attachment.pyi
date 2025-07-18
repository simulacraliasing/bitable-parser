from ..model.get_interview_record_attachment_request import GetInterviewRecordAttachmentRequest as GetInterviewRecordAttachmentRequest
from ..model.get_interview_record_attachment_response import GetInterviewRecordAttachmentResponse as GetInterviewRecordAttachmentResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class InterviewRecordAttachment:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetInterviewRecordAttachmentRequest, option: RequestOption | None = None) -> GetInterviewRecordAttachmentResponse: ...
    async def aget(self, request: GetInterviewRecordAttachmentRequest, option: RequestOption | None = None) -> GetInterviewRecordAttachmentResponse: ...
