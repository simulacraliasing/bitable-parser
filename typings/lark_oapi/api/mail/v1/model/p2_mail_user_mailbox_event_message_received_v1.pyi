from .subscriber import Subscriber as Subscriber
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2MailUserMailboxEventMessageReceivedV1Data:
    mail_address: str | None
    message_id: str | None
    mailbox_type: int | None
    subscriber: Subscriber | None
    def __init__(self, d=None) -> None: ...

class P2MailUserMailboxEventMessageReceivedV1(EventContext):
    event: P2MailUserMailboxEventMessageReceivedV1Data | None
    def __init__(self, d=None) -> None: ...
