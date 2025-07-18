from .list_admin_dept_stat_response_body import ListAdminDeptStatResponseBody as ListAdminDeptStatResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAdminDeptStatResponse(BaseResponse):
    data: ListAdminDeptStatResponseBody | None
    def __init__(self, d=None) -> None: ...
