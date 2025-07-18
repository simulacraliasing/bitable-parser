from .stream_recognize_speech_request_body import StreamRecognizeSpeechRequestBody as StreamRecognizeSpeechRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class StreamRecognizeSpeechRequest(BaseRequest):
    request_body: StreamRecognizeSpeechRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> StreamRecognizeSpeechRequestBuilder: ...

class StreamRecognizeSpeechRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: StreamRecognizeSpeechRequestBody) -> StreamRecognizeSpeechRequestBuilder: ...
    def build(self) -> StreamRecognizeSpeechRequest: ...
