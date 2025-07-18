from .application_stage_info import ApplicationStageInfo as ApplicationStageInfo
from .talent_tag import TalentTag as TalentTag
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireTalentTagSubscriptionV1Data:
    talent_id: str | None
    application_id: str | None
    type: int | None
    tag: TalentTag | None
    lock_status: int | None
    application_stage: ApplicationStageInfo | None
    def __init__(self, d=None) -> None: ...

class P2HireTalentTagSubscriptionV1(EventContext):
    event: P2HireTalentTagSubscriptionV1Data | None
    def __init__(self, d=None) -> None: ...
