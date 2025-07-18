from lark_oapi.core.construct import init as init

class File:
    url: str | None
    file_size: int | None
    title: str | None
    type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FileBuilder: ...

class FileBuilder:
    def __init__(self) -> None: ...
    def url(self, url: str) -> FileBuilder: ...
    def file_size(self, file_size: int) -> FileBuilder: ...
    def title(self, title: str) -> FileBuilder: ...
    def type(self, type: str) -> FileBuilder: ...
    def build(self) -> File: ...
