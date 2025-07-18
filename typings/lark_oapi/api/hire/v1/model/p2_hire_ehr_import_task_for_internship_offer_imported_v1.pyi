from .department_id import DepartmentId as DepartmentId
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireEhrImportTaskForInternshipOfferImportedV1Data:
    task_id: str | None
    application_id: str | None
    offer_id: str | None
    pre_onboard_id: str | None
    ehr_department_id: str | None
    operator_id: str | None
    operator_user_id: UserId | None
    ehr_department: DepartmentId | None
    def __init__(self, d=None) -> None: ...

class P2HireEhrImportTaskForInternshipOfferImportedV1(EventContext):
    event: P2HireEhrImportTaskForInternshipOfferImportedV1Data | None
    def __init__(self, d=None) -> None: ...
