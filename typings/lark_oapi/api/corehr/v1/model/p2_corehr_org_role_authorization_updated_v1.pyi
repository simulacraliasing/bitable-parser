from .management_scope import ManagementScope as ManagementScope
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrOrgRoleAuthorizationUpdatedV1Data:
    role_id: str | None
    management_scope_list: list[ManagementScope] | None
    employment_id_list: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrOrgRoleAuthorizationUpdatedV1(EventContext):
    event: P2CorehrOrgRoleAuthorizationUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
