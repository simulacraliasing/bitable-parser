from .batch_create_permission_member_response_body import BatchCreatePermissionMemberResponseBody as BatchCreatePermissionMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreatePermissionMemberResponse(BaseResponse):
    data: BatchCreatePermissionMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
