from lark_oapi.core.construct import init as init

class DownloadFileResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DownloadFileResponseBodyBuilder: ...

class DownloadFileResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DownloadFileResponseBody: ...
