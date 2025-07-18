from .custom_attr_event import CustomAttrEvent as CustomAttrEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactCustomAttrEventUpdatedV3Data:
    object: CustomAttrEvent | None
    old_object: CustomAttrEvent | None
    def __init__(self, d=None) -> None: ...

class P2ContactCustomAttrEventUpdatedV3(EventContext):
    event: P2ContactCustomAttrEventUpdatedV3Data | None
    def __init__(self, d=None) -> None: ...
