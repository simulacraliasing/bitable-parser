from .eco_exam_create_event_candidate_info import EcoExamCreateEventCandidateInfo as EcoExamCreateEventCandidateInfo
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireEcoExamCreatedV1Data:
    exam_id: str | None
    account_id: str | None
    paper_id: str | None
    candidate_info: EcoExamCreateEventCandidateInfo | None
    def __init__(self, d=None) -> None: ...

class P2HireEcoExamCreatedV1(EventContext):
    event: P2HireEcoExamCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
