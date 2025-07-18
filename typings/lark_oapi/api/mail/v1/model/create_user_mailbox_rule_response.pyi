from .create_user_mailbox_rule_response_body import CreateUserMailboxRuleResponseBody as CreateUserMailboxRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateUserMailboxRuleResponse(BaseResponse):
    data: CreateUserMailboxRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
