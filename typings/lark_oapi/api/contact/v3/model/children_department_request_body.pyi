from lark_oapi.core.construct import init as init

class ChildrenDepartmentRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ChildrenDepartmentRequestBodyBuilder: ...

class ChildrenDepartmentRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ChildrenDepartmentRequestBody: ...
