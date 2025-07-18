from .user_stats_fields_query_archive_rule_response_body import UserStatsFieldsQueryArchiveRuleResponseBody as UserStatsFieldsQueryArchiveRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UserStatsFieldsQueryArchiveRuleResponse(BaseResponse):
    data: UserStatsFieldsQueryArchiveRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
