from ..model.get_interview_record_request import GetInterviewRecordRequest as GetInterviewRecordRequest
from ..model.get_interview_record_response import GetInterviewRecordResponse as GetInterviewRecordResponse
from ..model.list_interview_record_request import ListInterviewRecordRequest as ListInterviewRecordRequest
from ..model.list_interview_record_response import ListInterviewRecordResponse as ListInterviewRecordResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class InterviewRecord:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetInterviewRecordRequest, option: RequestOption | None = None) -> GetInterviewRecordResponse: ...
    async def aget(self, request: GetInterviewRecordRequest, option: RequestOption | None = None) -> GetInterviewRecordResponse: ...
    def list(self, request: ListInterviewRecordRequest, option: RequestOption | None = None) -> ListInterviewRecordResponse: ...
    async def alist(self, request: ListInterviewRecordRequest, option: RequestOption | None = None) -> ListInterviewRecordResponse: ...
