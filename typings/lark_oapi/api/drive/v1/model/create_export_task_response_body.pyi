from lark_oapi.core.construct import init as init

class CreateExportTaskResponseBody:
    ticket: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateExportTaskResponseBodyBuilder: ...

class CreateExportTaskResponseBodyBuilder:
    def __init__(self) -> None: ...
    def ticket(self, ticket: str) -> CreateExportTaskResponseBodyBuilder: ...
    def build(self) -> CreateExportTaskResponseBody: ...
