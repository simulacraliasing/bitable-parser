from .list_functional_role_member_response_body import ListFunctionalRoleMemberResponseBody as ListFunctionalRoleMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFunctionalRoleMemberResponse(BaseResponse):
    data: ListFunctionalRoleMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
