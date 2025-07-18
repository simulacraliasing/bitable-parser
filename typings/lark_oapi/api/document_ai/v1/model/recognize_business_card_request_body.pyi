from lark_oapi.core.construct import init as init
from typing import Any, IO

class RecognizeBusinessCardRequestBody:
    file: IO[Any] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RecognizeBusinessCardRequestBodyBuilder: ...

class RecognizeBusinessCardRequestBodyBuilder:
    def __init__(self) -> None: ...
    def file(self, file: IO[Any]) -> RecognizeBusinessCardRequestBodyBuilder: ...
    def build(self) -> RecognizeBusinessCardRequestBody: ...
