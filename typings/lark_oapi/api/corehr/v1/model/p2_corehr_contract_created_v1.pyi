from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrContractCreatedV1Data:
    contract_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrContractCreatedV1(EventContext):
    event: P2CorehrContractCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
