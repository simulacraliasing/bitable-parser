from .department_overview_application_app_usage_response_body import DepartmentOverviewApplicationAppUsageResponseBody as DepartmentOverviewApplicationAppUsageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DepartmentOverviewApplicationAppUsageResponse(BaseResponse):
    data: DepartmentOverviewApplicationAppUsageResponseBody | None
    def __init__(self, d=None) -> None: ...
