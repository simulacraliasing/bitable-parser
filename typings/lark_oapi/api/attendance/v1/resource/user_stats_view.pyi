from ..model.query_user_stats_view_request import QueryUserStatsViewRequest as QueryUserStatsViewRequest
from ..model.query_user_stats_view_response import QueryUserStatsViewResponse as QueryUserStatsViewResponse
from ..model.update_user_stats_view_request import UpdateUserStatsViewRequest as UpdateUserStatsViewRequest
from ..model.update_user_stats_view_response import UpdateUserStatsViewResponse as UpdateUserStatsViewResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserStatsView:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def query(self, request: QueryUserStatsViewRequest, option: RequestOption | None = None) -> QueryUserStatsViewResponse: ...
    async def aquery(self, request: QueryUserStatsViewRequest, option: RequestOption | None = None) -> QueryUserStatsViewResponse: ...
    def update(self, request: UpdateUserStatsViewRequest, option: RequestOption | None = None) -> UpdateUserStatsViewResponse: ...
    async def aupdate(self, request: UpdateUserStatsViewRequest, option: RequestOption | None = None) -> UpdateUserStatsViewResponse: ...
