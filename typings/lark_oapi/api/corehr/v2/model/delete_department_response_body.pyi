from lark_oapi.core.construct import init as init

class DeleteDepartmentResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteDepartmentResponseBodyBuilder: ...

class DeleteDepartmentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteDepartmentResponseBody: ...
