from .list_mailgroup_permission_member_response_body import ListMailgroupPermissionMemberResponseBody as ListMailgroupPermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMailgroupPermissionMemberResponse(BaseResponse):
    data: ListMailgroupPermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
