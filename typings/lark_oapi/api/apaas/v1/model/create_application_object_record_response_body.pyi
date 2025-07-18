from lark_oapi.core.construct import init as init

class CreateApplicationObjectRecordResponseBody:
    id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateApplicationObjectRecordResponseBodyBuilder: ...

class CreateApplicationObjectRecordResponseBodyBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> CreateApplicationObjectRecordResponseBodyBuilder: ...
    def build(self) -> CreateApplicationObjectRecordResponseBody: ...
