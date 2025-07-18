from .list_period_rule_response_body import ListPeriodRuleResponseBody as ListPeriodRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPeriodRuleResponse(BaseResponse):
    data: ListPeriodRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
