from .list_app_role_response_body import ListAppRoleResponseBody as ListAppRoleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppRoleResponse(BaseResponse):
    data: ListAppRoleResponseBody | None
    def __init__(self, d=None) -> None: ...
