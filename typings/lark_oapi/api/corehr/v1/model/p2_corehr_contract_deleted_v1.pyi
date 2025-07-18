from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrContractDeletedV1Data:
    contract_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrContractDeletedV1(EventContext):
    event: P2CorehrContractDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
