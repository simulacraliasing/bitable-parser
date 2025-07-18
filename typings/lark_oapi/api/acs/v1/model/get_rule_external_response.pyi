from .get_rule_external_response_body import GetRuleExternalResponseBody as GetRuleExternalResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetRuleExternalResponse(BaseResponse):
    data: GetRuleExternalResponseBody | None
    def __init__(self, d=None) -> None: ...
