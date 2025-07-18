from lark_oapi.core.construct import init as init

class Media:
    file_token: str | None
    file_name: str | None
    size: int | None
    mime_type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MediaBuilder: ...

class MediaBuilder:
    def __init__(self) -> None: ...
    def file_token(self, file_token: str) -> MediaBuilder: ...
    def file_name(self, file_name: str) -> MediaBuilder: ...
    def size(self, size: int) -> MediaBuilder: ...
    def mime_type(self, mime_type: str) -> MediaBuilder: ...
    def build(self) -> Media: ...
