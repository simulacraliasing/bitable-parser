from .overview_application_app_usage_response_body import OverviewApplicationAppUsageResponseBody as OverviewApplicationAppUsageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class OverviewApplicationAppUsageResponse(BaseResponse):
    data: OverviewApplicationAppUsageResponseBody | None
    def __init__(self, d=None) -> None: ...
