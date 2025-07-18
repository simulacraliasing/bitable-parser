from ..model.list_interviewer_request import ListInterviewerRequest as ListInterviewerRequest
from ..model.list_interviewer_response import ListInterviewerResponse as ListInterviewerResponse
from ..model.patch_interviewer_request import PatchInterviewerRequest as PatchInterviewerRequest
from ..model.patch_interviewer_response import PatchInterviewerResponse as PatchInterviewerResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Interviewer:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListInterviewerRequest, option: RequestOption | None = None) -> ListInterviewerResponse: ...
    async def alist(self, request: ListInterviewerRequest, option: RequestOption | None = None) -> ListInterviewerResponse: ...
    def patch(self, request: PatchInterviewerRequest, option: RequestOption | None = None) -> PatchInterviewerResponse: ...
    async def apatch(self, request: PatchInterviewerRequest, option: RequestOption | None = None) -> PatchInterviewerResponse: ...
