from lark_oapi.core.construct import init as init

class DownloadToken:
    token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DownloadTokenBuilder: ...

class DownloadTokenBuilder:
    def __init__(self) -> None: ...
    def token(self, token: str) -> DownloadTokenBuilder: ...
    def build(self) -> DownloadToken: ...
