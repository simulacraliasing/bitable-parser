from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrOffboardingUpdatedV2Data:
    tenant_id: str | None
    offboarding_info_id: str | None
    process_id: str | None
    checklist_process_id: str | None
    employment_id: str | None
    operator: str | None
    status: int | None
    checklist_status: int | None
    updated_time: str | None
    updated_fields: list[str] | None
    target_user_id: UserId | None
    def __init__(self, d=None) -> None: ...

class P2CorehrOffboardingUpdatedV2(EventContext):
    event: P2CorehrOffboardingUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
