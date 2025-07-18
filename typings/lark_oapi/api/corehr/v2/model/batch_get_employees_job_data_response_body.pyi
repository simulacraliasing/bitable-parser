from .employee_job_data import EmployeeJobData as EmployeeJobData
from lark_oapi.core.construct import init as init

class BatchGetEmployeesJobDataResponseBody:
    items: list[EmployeeJobData] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchGetEmployeesJobDataResponseBodyBuilder: ...

class BatchGetEmployeesJobDataResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[EmployeeJobData]) -> BatchGetEmployeesJobDataResponseBodyBuilder: ...
    def build(self) -> BatchGetEmployeesJobDataResponseBody: ...
