from .name import Name as Name
from .org_truncation import OrgTruncation as OrgTruncation
from lark_oapi.core.construct import init as init

class SecurityGroup:
    id: str | None
    code: str | None
    name: Name | None
    active_status: int | None
    description: Name | None
    group_type: int | None
    created_by: str | None
    update_time: str | None
    org_truncation: list[OrgTruncation] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SecurityGroupBuilder: ...

class SecurityGroupBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> SecurityGroupBuilder: ...
    def code(self, code: str) -> SecurityGroupBuilder: ...
    def name(self, name: Name) -> SecurityGroupBuilder: ...
    def active_status(self, active_status: int) -> SecurityGroupBuilder: ...
    def description(self, description: Name) -> SecurityGroupBuilder: ...
    def group_type(self, group_type: int) -> SecurityGroupBuilder: ...
    def created_by(self, created_by: str) -> SecurityGroupBuilder: ...
    def update_time(self, update_time: str) -> SecurityGroupBuilder: ...
    def org_truncation(self, org_truncation: list[OrgTruncation]) -> SecurityGroupBuilder: ...
    def build(self) -> SecurityGroup: ...
