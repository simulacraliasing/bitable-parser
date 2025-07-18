from .list_role_response_body import ListRoleResponseBody as ListRoleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListRoleResponse(BaseResponse):
    data: ListRoleResponseBody | None
    def __init__(self, d=None) -> None: ...
