from .list_admin_user_stat_response_body import ListAdminUserStatResponseBody as ListAdminUserStatResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAdminUserStatResponse(BaseResponse):
    data: ListAdminUserStatResponseBody | None
    def __init__(self, d=None) -> None: ...
