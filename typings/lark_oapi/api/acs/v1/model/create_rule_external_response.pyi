from .create_rule_external_response_body import CreateRuleExternalResponseBody as CreateRuleExternalResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateRuleExternalResponse(BaseResponse):
    data: CreateRuleExternalResponseBody | None
    def __init__(self, d=None) -> None: ...
