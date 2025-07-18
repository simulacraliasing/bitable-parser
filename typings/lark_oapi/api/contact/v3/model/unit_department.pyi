from lark_oapi.core.construct import init as init

class UnitDepartment:
    unit_id: str | None
    department_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UnitDepartmentBuilder: ...

class UnitDepartmentBuilder:
    def __init__(self) -> None: ...
    def unit_id(self, unit_id: str) -> UnitDepartmentBuilder: ...
    def department_id(self, department_id: str) -> UnitDepartmentBuilder: ...
    def build(self) -> UnitDepartment: ...
