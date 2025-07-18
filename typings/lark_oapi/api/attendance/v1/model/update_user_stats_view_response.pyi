from .update_user_stats_view_response_body import UpdateUserStatsViewResponseBody as UpdateUserStatsViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateUserStatsViewResponse(BaseResponse):
    data: UpdateUserStatsViewResponseBody | None
    def __init__(self, d=None) -> None: ...
