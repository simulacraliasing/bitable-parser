from ..model.list_application_interview_request import ListApplicationInterviewRequest as ListApplicationInterviewRequest
from ..model.list_application_interview_response import ListApplicationInterviewResponse as ListApplicationInterviewResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ApplicationInterview:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListApplicationInterviewRequest, option: RequestOption | None = None) -> ListApplicationInterviewResponse: ...
    async def alist(self, request: ListApplicationInterviewRequest, option: RequestOption | None = None) -> ListApplicationInterviewResponse: ...
