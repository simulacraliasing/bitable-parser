from .batch_create_mailgroup_permission_member_response_body import BatchCreateMailgroupPermissionMemberResponseBody as BatchCreateMailgroupPermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateMailgroupPermissionMemberResponse(BaseResponse):
    data: BatchCreateMailgroupPermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
