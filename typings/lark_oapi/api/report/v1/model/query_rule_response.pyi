from .query_rule_response_body import QueryRuleResponseBody as QueryRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRuleResponse(BaseResponse):
    data: QueryRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
