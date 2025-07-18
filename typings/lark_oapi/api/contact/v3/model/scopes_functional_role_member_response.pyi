from .scopes_functional_role_member_response_body import ScopesFunctionalRoleMemberResponseBody as ScopesFunctionalRoleMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ScopesFunctionalRoleMemberResponse(BaseResponse):
    data: ScopesFunctionalRoleMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
