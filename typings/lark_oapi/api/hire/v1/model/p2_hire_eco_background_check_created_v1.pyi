from .eco_background_check_create_event_candidate_info import EcoBackgroundCheckCreateEventCandidateInfo as EcoBackgroundCheckCreateEventCandidateInfo
from .eco_background_check_create_event_contact_info import EcoBackgroundCheckCreateEventContactInfo as EcoBackgroundCheckCreateEventContactInfo
from .eco_background_check_create_event_custom_kv import EcoBackgroundCheckCreateEventCustomKv as EcoBackgroundCheckCreateEventCustomKv
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireEcoBackgroundCheckCreatedV1Data:
    background_check_id: str | None
    account_id: str | None
    package_id: str | None
    additional_item_id_list: list[str] | None
    comment: str | None
    candidate_info: EcoBackgroundCheckCreateEventCandidateInfo | None
    client_contact_info: EcoBackgroundCheckCreateEventContactInfo | None
    custom_field_list: list[EcoBackgroundCheckCreateEventCustomKv] | None
    def __init__(self, d=None) -> None: ...

class P2HireEcoBackgroundCheckCreatedV1(EventContext):
    event: P2HireEcoBackgroundCheckCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
