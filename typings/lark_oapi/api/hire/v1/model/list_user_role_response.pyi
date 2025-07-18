from .list_user_role_response_body import ListUserRoleResponseBody as ListUserRoleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUserRoleResponse(BaseResponse):
    data: ListUserRoleResponseBody | None
    def __init__(self, d=None) -> None: ...
