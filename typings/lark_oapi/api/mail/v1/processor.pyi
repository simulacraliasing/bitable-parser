from .model.p2_mail_user_mailbox_event_message_received_v1 import P2MailUserMailboxEventMessageReceivedV1 as P2MailUserMailboxEventMessageReceivedV1
from _typeshed import Incomplete
from lark_oapi.event.processor import IEventProcessor as IEventProcessor
from typing import Callable

class P2MailUserMailboxEventMessageReceivedV1Processor(IEventProcessor[P2MailUserMailboxEventMessageReceivedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2MailUserMailboxEventMessageReceivedV1], None]) -> None: ...
    def type(self) -> type[P2MailUserMailboxEventMessageReceivedV1]: ...
    def do(self, data: P2MailUserMailboxEventMessageReceivedV1) -> None: ...
