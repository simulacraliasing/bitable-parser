from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrJobChangeStatusUpdatedV2Data:
    employment_id: str | None
    target_user_id: UserId | None
    job_change_id: str | None
    transfer_mode: int | None
    transfer_type_unique_identifier: str | None
    transfer_reason_unique_identifier: str | None
    process_id: str | None
    effective_date: str | None
    status: int | None
    transfer_key: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrJobChangeStatusUpdatedV2(EventContext):
    event: P2CorehrJobChangeStatusUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
