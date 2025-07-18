from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobChangeUpdatedV2Data:
    employment_id: str | None
    tenant_id: str | None
    process_id: str | None
    initiator: str | None
    operator: str | None
    updated_time: str | None
    job_change_id: str | None
    status: int | None
    operate_reason: str | None
    transfer_type: int | None
    updated_fields: list[str] | None
    transform_type: str | None
    transform_reason: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobChangeUpdatedV2(EventContext):
    event: P2CorehrJobChangeUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
