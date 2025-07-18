from ..model.file_recognize_speech_request import FileRecognizeSpeechRequest as FileRecognizeSpeechRequest
from ..model.file_recognize_speech_response import FileRecognizeSpeechResponse as FileRecognizeSpeechResponse
from ..model.stream_recognize_speech_request import StreamRecognizeSpeechRequest as StreamRecognizeSpeechRequest
from ..model.stream_recognize_speech_response import StreamRecognizeSpeechResponse as StreamRecognizeSpeechResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Speech:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def file_recognize(self, request: FileRecognizeSpeechRequest, option: RequestOption | None = None) -> FileRecognizeSpeechResponse: ...
    async def afile_recognize(self, request: FileRecognizeSpeechRequest, option: RequestOption | None = None) -> FileRecognizeSpeechResponse: ...
    def stream_recognize(self, request: StreamRecognizeSpeechRequest, option: RequestOption | None = None) -> StreamRecognizeSpeechResponse: ...
    async def astream_recognize(self, request: StreamRecognizeSpeechRequest, option: RequestOption | None = None) -> StreamRecognizeSpeechResponse: ...
