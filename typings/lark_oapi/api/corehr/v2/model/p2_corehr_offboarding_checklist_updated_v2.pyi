from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrOffboardingChecklistUpdatedV2Data:
    employment_id: str | None
    target_user_id: UserId | None
    offboarding_id: str | None
    checklist_process_id: str | None
    checklist_status: int | None
    def __init__(self, d=None) -> None: ...

class P2CorehrOffboardingChecklistUpdatedV2(EventContext):
    event: P2CorehrOffboardingChecklistUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
