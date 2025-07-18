from .customized_field_display_item import CustomizedFieldDisplayItem as CustomizedFieldDisplayItem
from .ticket_user_event import TicketUserEvent as TicketUserEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HelpdeskTicketCreatedV1Data:
    ticket_id: str | None
    helpdesk_id: str | None
    guest: TicketUserEvent | None
    stage: int | None
    status: int | None
    score: int | None
    created_at: int | None
    updated_at: int | None
    closed_at: int | None
    channel: int | None
    solve: int | None
    customized_fields: list[CustomizedFieldDisplayItem] | None
    chat_id: str | None
    def __init__(self, d=None) -> None: ...

class P2HelpdeskTicketCreatedV1(EventContext):
    event: P2HelpdeskTicketCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
