from .application_department_app_usage import ApplicationDepartmentAppUsage as ApplicationDepartmentAppUsage
from lark_oapi.core.construct import init as init

class DepartmentOverviewApplicationAppUsageResponseBody:
    has_more: bool | None
    page_token: str | None
    items: list[ApplicationDepartmentAppUsage] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DepartmentOverviewApplicationAppUsageResponseBodyBuilder: ...

class DepartmentOverviewApplicationAppUsageResponseBodyBuilder:
    def __init__(self) -> None: ...
    def has_more(self, has_more: bool) -> DepartmentOverviewApplicationAppUsageResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> DepartmentOverviewApplicationAppUsageResponseBodyBuilder: ...
    def items(self, items: list[ApplicationDepartmentAppUsage]) -> DepartmentOverviewApplicationAppUsageResponseBodyBuilder: ...
    def build(self) -> DepartmentOverviewApplicationAppUsageResponseBody: ...
