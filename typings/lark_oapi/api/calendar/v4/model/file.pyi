from lark_oapi.core.construct import init as init

class File:
    file_token: str | None
    file_size: str | None
    name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FileBuilder: ...

class FileBuilder:
    def __init__(self) -> None: ...
    def file_token(self, file_token: str) -> FileBuilder: ...
    def file_size(self, file_size: str) -> FileBuilder: ...
    def name(self, name: str) -> FileBuilder: ...
    def build(self) -> File: ...
