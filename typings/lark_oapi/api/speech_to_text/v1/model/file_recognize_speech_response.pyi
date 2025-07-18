from .file_recognize_speech_response_body import FileRecognizeSpeechResponseBody as FileRecognizeSpeechResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class FileRecognizeSpeechResponse(BaseResponse):
    data: FileRecognizeSpeechResponseBody | None
    def __init__(self, d=None) -> None: ...
