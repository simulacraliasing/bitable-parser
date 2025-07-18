from .get_approval_groups_response_body import GetApprovalGroupsResponseBody as GetApprovalGroupsResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetApprovalGroupsResponse(BaseResponse):
    data: GetApprovalGroupsResponseBody | None
    def __init__(self, d=None) -> None: ...
