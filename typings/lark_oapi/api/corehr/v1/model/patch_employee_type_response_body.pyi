from .employee_type import EmployeeType as EmployeeType
from lark_oapi.core.construct import init as init

class PatchEmployeeTypeResponseBody:
    employee_type: EmployeeType | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchEmployeeTypeResponseBodyBuilder: ...

class PatchEmployeeTypeResponseBodyBuilder:
    def __init__(self) -> None: ...
    def employee_type(self, employee_type: EmployeeType) -> PatchEmployeeTypeResponseBodyBuilder: ...
    def build(self) -> PatchEmployeeTypeResponseBody: ...
