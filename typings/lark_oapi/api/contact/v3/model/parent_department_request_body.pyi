from lark_oapi.core.construct import init as init

class ParentDepartmentRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ParentDepartmentRequestBodyBuilder: ...

class ParentDepartmentRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ParentDepartmentRequestBody: ...
