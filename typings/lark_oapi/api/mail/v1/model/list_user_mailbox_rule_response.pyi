from .list_user_mailbox_rule_response_body import ListUserMailboxRuleResponseBody as ListUserMailboxRuleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUserMailboxRuleResponse(BaseResponse):
    data: ListUserMailboxRuleResponseBody | None
    def __init__(self, d=None) -> None: ...
