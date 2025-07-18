from .get_functional_role_member_response_body import GetFunctionalRoleMemberResponseBody as GetFunctionalRoleMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetFunctionalRoleMemberResponse(BaseResponse):
    data: GetFunctionalRoleMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
