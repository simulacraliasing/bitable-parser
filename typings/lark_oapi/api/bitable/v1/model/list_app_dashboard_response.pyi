from .list_app_dashboard_response_body import ListAppDashboardResponseBody as ListAppDashboardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppDashboardResponse(BaseResponse):
    data: ListAppDashboardResponseBody | None
    def __init__(self, d=None) -> None: ...
