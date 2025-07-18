from .list_app_role_member_response_body import ListAppRoleMemberResponseBody as ListAppRoleMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppRoleMemberResponse(BaseResponse):
    data: ListAppRoleMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
