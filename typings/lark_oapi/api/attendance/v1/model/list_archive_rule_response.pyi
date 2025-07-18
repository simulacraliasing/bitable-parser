from .list_archive_rule_response_body import ListArchiveRuleResponseBody as ListArchiveRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListArchiveRuleResponse(BaseResponse):
    data: ListArchiveRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
