from .eco_account_custom_field_event_data import EcoAccountCustomFieldEventData as EcoAccountCustomFieldEventData
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireEcoAccountCreatedV1Data:
    scope: int | None
    account_id: str | None
    account_name: str | None
    usage_list: list[int] | None
    custom_field_list: list[EcoAccountCustomFieldEventData] | None
    def __init__(self, d=None) -> None: ...

class P2HireEcoAccountCreatedV1(EventContext):
    event: P2HireEcoAccountCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
