from .list_app_recommend_rule_response_body import ListAppRecommendRuleResponseBody as ListAppRecommendRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppRecommendRuleResponse(BaseResponse):
    data: ListAppRecommendRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
