from lark_oapi.core.construct import init as init

class DeleteFileRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteFileRequestBodyBuilder: ...

class DeleteFileRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteFileRequestBody: ...
