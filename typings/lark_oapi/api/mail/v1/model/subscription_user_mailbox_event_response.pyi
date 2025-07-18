from .subscription_user_mailbox_event_response_body import SubscriptionUserMailboxEventResponseBody as SubscriptionUserMailboxEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SubscriptionUserMailboxEventResponse(BaseResponse):
    data: SubscriptionUserMailboxEventResponseBody | None
    def __init__(self, d=None) -> None: ...
