from .role_member import RoleMember as RoleMember
from lark_oapi.core.construct import init as init

class GetApplicationRoleMemberResponseBody:
    role_member: RoleMember | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetApplicationRoleMemberResponseBodyBuilder: ...

class GetApplicationRoleMemberResponseBodyBuilder:
    def __init__(self) -> None: ...
    def role_member(self, role_member: RoleMember) -> GetApplicationRoleMemberResponseBodyBuilder: ...
    def build(self) -> GetApplicationRoleMemberResponseBody: ...
