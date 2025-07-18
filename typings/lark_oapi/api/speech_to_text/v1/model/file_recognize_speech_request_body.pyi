from .file_config import FileConfig as FileConfig
from .speech import Speech as Speech
from lark_oapi.core.construct import init as init

class FileRecognizeSpeechRequestBody:
    speech: Speech | None
    config: FileConfig | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FileRecognizeSpeechRequestBodyBuilder: ...

class FileRecognizeSpeechRequestBodyBuilder:
    def __init__(self) -> None: ...
    def speech(self, speech: Speech) -> FileRecognizeSpeechRequestBodyBuilder: ...
    def config(self, config: FileConfig) -> FileRecognizeSpeechRequestBodyBuilder: ...
    def build(self) -> FileRecognizeSpeechRequestBody: ...
