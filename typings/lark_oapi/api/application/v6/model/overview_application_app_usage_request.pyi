from .overview_application_app_usage_request_body import OverviewApplicationAppUsageRequestBody as OverviewApplicationAppUsageRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class OverviewApplicationAppUsageRequest(BaseRequest):
    department_id_type: str | None
    app_id: str | None
    request_body: OverviewApplicationAppUsageRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> OverviewApplicationAppUsageRequestBuilder: ...

class OverviewApplicationAppUsageRequestBuilder:
    def __init__(self) -> None: ...
    def department_id_type(self, department_id_type: str) -> OverviewApplicationAppUsageRequestBuilder: ...
    def app_id(self, app_id: str) -> OverviewApplicationAppUsageRequestBuilder: ...
    def request_body(self, request_body: OverviewApplicationAppUsageRequestBody) -> OverviewApplicationAppUsageRequestBuilder: ...
    def build(self) -> OverviewApplicationAppUsageRequest: ...
