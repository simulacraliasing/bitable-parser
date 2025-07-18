from typing import *
from lark_oapi.core.construct import init as init

class EventHeader:
    event_id: Optional[str]
    token: Optional[str]
    create_time: Optional[str]
    event_type: Optional[str]
    tenant_key: Optional[str]
    app_id: Optional[str]
    def __init__(self, d=None) -> None: ...

class EventContext:
    challenge: Optional[str]
    ts: Optional[str]
    uuid: Optional[str]
    token: Optional[str]
    type: Optional[str]
    schema: Optional[str]
    header: Optional[EventHeader]
    event: Dict
    def __init__(self, d=None) -> None: ...
