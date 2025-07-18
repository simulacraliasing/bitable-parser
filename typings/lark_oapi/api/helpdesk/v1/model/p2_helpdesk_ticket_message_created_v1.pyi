from .ticket import Ticket as Ticket
from .ticket_message_content import TicketMessageContent as TicketMessageContent
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HelpdeskTicketMessageCreatedV1Data:
    ticket_message_id: str | None
    message_id: str | None
    msg_type: str | None
    position: str | None
    sender_id: UserId | None
    sender_type: int | None
    text: str | None
    ticket: Ticket | None
    event_id: str | None
    chat_id: str | None
    content: TicketMessageContent | None
    def __init__(self, d=None) -> None: ...

class P2HelpdeskTicketMessageCreatedV1(EventContext):
    event: P2HelpdeskTicketMessageCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
