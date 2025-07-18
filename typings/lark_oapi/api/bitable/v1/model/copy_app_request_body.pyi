from lark_oapi.core.construct import init as init

class CopyAppRequestBody:
    name: str | None
    folder_token: str | None
    without_content: bool | None
    time_zone: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CopyAppRequestBodyBuilder: ...

class CopyAppRequestBodyBuilder:
    def __init__(self) -> None: ...
    def name(self, name: str) -> CopyAppRequestBodyBuilder: ...
    def folder_token(self, folder_token: str) -> CopyAppRequestBodyBuilder: ...
    def without_content(self, without_content: bool) -> CopyAppRequestBodyBuilder: ...
    def time_zone(self, time_zone: str) -> CopyAppRequestBodyBuilder: ...
    def build(self) -> CopyAppRequestBody: ...
