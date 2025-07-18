from ..model.parse_resume_request import ParseResumeRequest as ParseResumeRequest
from ..model.parse_resume_response import ParseResumeResponse as ParseResumeResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class Resume:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def parse(self, request: ParseResumeRequest, option: RequestOption | None = None) -> ParseResumeResponse: ...
    async def aparse(self, request: ParseResumeRequest, option: RequestOption | None = None) -> ParseResumeResponse: ...
