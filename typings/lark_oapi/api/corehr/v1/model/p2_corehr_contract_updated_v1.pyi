from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrContractUpdatedV1Data:
    contract_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrContractUpdatedV1(EventContext):
    event: P2CorehrContractUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
