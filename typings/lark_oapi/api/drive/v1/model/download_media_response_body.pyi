from lark_oapi.core.construct import init as init

class DownloadMediaResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DownloadMediaResponseBodyBuilder: ...

class DownloadMediaResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DownloadMediaResponseBody: ...
