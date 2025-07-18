from .organization_domain_event_data import OrganizationDomainEventData as OrganizationDomainEventData
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrCompanyUpdatedV2Data:
    company_id: str | None
    field_changes: list[str] | None
    sub_events: list[OrganizationDomainEventData] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrCompanyUpdatedV2(EventContext):
    event: P2CorehrCompanyUpdatedV2Data | None
    def __init__(self, d=None) -> None: ...
