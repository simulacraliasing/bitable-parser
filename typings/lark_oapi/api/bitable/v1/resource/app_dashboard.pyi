from ..model.copy_app_dashboard_request import CopyAppDashboardRequest as CopyAppDashboardRequest
from ..model.copy_app_dashboard_response import CopyAppDashboardResponse as CopyAppDashboardResponse
from ..model.list_app_dashboard_request import ListAppDashboardRequest as ListAppDashboardRequest
from ..model.list_app_dashboard_response import ListAppDashboardResponse as ListAppDashboardResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AppDashboard:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def copy(self, request: CopyAppDashboardRequest, option: RequestOption | None = None) -> CopyAppDashboardResponse: ...
    async def acopy(self, request: CopyAppDashboardRequest, option: RequestOption | None = None) -> CopyAppDashboardResponse: ...
    def list(self, request: ListAppDashboardRequest, option: RequestOption | None = None) -> ListAppDashboardResponse: ...
    async def alist(self, request: ListAppDashboardRequest, option: RequestOption | None = None) -> ListAppDashboardResponse: ...
