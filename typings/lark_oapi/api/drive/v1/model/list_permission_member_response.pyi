from .list_permission_member_response_body import ListPermissionMemberResponseBody as ListPermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPermissionMemberResponse(BaseResponse):
    data: ListPermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
