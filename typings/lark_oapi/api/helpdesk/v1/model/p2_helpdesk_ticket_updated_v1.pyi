from .ticket_event import TicketEvent as TicketEvent
from .ticket_event_update_info import TicketEventUpdateInfo as TicketEventUpdateInfo
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HelpdeskTicketUpdatedV1Data:
    object: TicketEvent | None
    old_object: TicketEventUpdateInfo | None
    def __init__(self, d=None) -> None: ...

class P2HelpdeskTicketUpdatedV1(EventContext):
    event: P2HelpdeskTicketUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
