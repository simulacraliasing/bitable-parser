from lark_oapi.core.construct import init as init

class DownloadExportTaskRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DownloadExportTaskRequestBodyBuilder: ...

class DownloadExportTaskRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DownloadExportTaskRequestBody: ...
