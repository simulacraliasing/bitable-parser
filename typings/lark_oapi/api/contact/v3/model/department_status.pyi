from lark_oapi.core.construct import init as init

class DepartmentStatus:
    is_deleted: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DepartmentStatusBuilder: ...

class DepartmentStatusBuilder:
    def __init__(self) -> None: ...
    def is_deleted(self, is_deleted: bool) -> DepartmentStatusBuilder: ...
    def build(self) -> DepartmentStatus: ...
