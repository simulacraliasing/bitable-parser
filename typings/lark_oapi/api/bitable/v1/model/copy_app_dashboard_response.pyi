from .copy_app_dashboard_response_body import CopyAppDashboardResponseBody as CopyAppDashboardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CopyAppDashboardResponse(BaseResponse):
    data: CopyAppDashboardResponseBody | None
    def __init__(self, d=None) -> None: ...
