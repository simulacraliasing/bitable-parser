from lark_oapi.core.construct import init as init

class ListAccessRecordRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListAccessRecordRequestBodyBuilder: ...

class ListAccessRecordRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListAccessRecordRequestBody: ...
