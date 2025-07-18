from ..model.get_minute_transcript_request import GetMinuteTranscriptRequest as GetMinuteTranscriptRequest
from ..model.get_minute_transcript_response import GetMinuteTranscriptResponse as GetMinuteTranscriptResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class MinuteTranscript:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetMinuteTranscriptRequest, option: RequestOption | None = None) -> GetMinuteTranscriptResponse: ...
    async def aget(self, request: GetMinuteTranscriptRequest, option: RequestOption | None = None) -> GetMinuteTranscriptResponse: ...
