from .batch_add_group_member_response_body import BatchAddGroupMemberResponseBody as BatchAddGroupMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchAddGroupMemberResponse(BaseResponse):
    data: BatchAddGroupMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
