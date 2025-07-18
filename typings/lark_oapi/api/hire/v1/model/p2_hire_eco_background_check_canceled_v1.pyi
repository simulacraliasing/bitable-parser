from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireEcoBackgroundCheckCanceledV1Data:
    background_check_id: str | None
    termination_reason: str | None
    def __init__(self, d=None) -> None: ...

class P2HireEcoBackgroundCheckCanceledV1(EventContext):
    event: P2HireEcoBackgroundCheckCanceledV1Data | None
    def __init__(self, d=None) -> None: ...
