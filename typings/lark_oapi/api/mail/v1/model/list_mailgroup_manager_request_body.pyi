from lark_oapi.core.construct import init as init

class ListMailgroupManagerRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListMailgroupManagerRequestBodyBuilder: ...

class ListMailgroupManagerRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListMailgroupManagerRequestBody: ...
