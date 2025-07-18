from .batch_create_mailgroup_member_response_body import BatchCreateMailgroupMemberResponseBody as BatchCreateMailgroupMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateMailgroupMemberResponse(BaseResponse):
    data: BatchCreateMailgroupMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
