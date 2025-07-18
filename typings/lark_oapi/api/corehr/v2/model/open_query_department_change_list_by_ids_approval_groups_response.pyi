from .open_query_department_change_list_by_ids_approval_groups_response_body import OpenQueryDepartmentChangeListByIdsApprovalGroupsResponseBody as OpenQueryDepartmentChangeListByIdsApprovalGroupsResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class OpenQueryDepartmentChangeListByIdsApprovalGroupsResponse(BaseResponse):
    data: OpenQueryDepartmentChangeListByIdsApprovalGroupsResponseBody | None
    def __init__(self, d=None) -> None: ...
