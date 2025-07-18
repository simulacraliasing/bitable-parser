from .stream_recognize_speech_response_body import StreamRecognizeSpeechResponseBody as StreamRecognizeSpeechResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class StreamRecognizeSpeechResponse(BaseResponse):
    data: StreamRecognizeSpeechResponseBody | None
    def __init__(self, d=None) -> None: ...
