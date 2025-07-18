from lark_oapi.core.construct import init as init
from typing import Any, IO

class UploadPersonRequestBody:
    file_content: IO[Any] | None
    file_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UploadPersonRequestBodyBuilder: ...

class UploadPersonRequestBodyBuilder:
    def __init__(self) -> None: ...
    def file_content(self, file_content: IO[Any]) -> UploadPersonRequestBodyBuilder: ...
    def file_name(self, file_name: str) -> UploadPersonRequestBodyBuilder: ...
    def build(self) -> UploadPersonRequestBody: ...
