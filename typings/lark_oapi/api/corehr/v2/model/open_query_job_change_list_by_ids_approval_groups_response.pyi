from .open_query_job_change_list_by_ids_approval_groups_response_body import OpenQueryJobChangeListByIdsApprovalGroupsResponseBody as OpenQueryJobChangeListByIdsApprovalGroupsResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class OpenQueryJobChangeListByIdsApprovalGroupsResponse(BaseResponse):
    data: OpenQueryJobChangeListByIdsApprovalGroupsResponseBody | None
    def __init__(self, d=None) -> None: ...
